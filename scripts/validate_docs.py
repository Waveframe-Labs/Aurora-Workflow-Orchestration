#!/usr/bin/env python3
"""
Doc Guard — AWO/CRI-Compatible Documentation Validator
Non-blocking by default unless DOC_GUARD_STRICT=1.

Validates:
- YAML metadata blocks
- Required fields (filetype, version, license)
- Allowed filetypes
- Required top-level documentation files
- DOI correctness (concept DOI only)
- ADR reference existence
"""

import re, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]

# --------------------------------------------------------------
# CONFIGURATION
# --------------------------------------------------------------

CONCEPT_DOI = "10.5281/zenodo.17013612"
STRICT = (pathlib.os.environ.get("DOC_GUARD_STRICT", "0") == "1")

REQUIRED_METADATA_FIELDS = [
    "filetype",
    "version",
    "license",
]

ALLOWED_FILETYPES = {
    "doctrine",
    "specification",
    "documentation",
    "method_spec",
    "schema",
}

REQUIRED_TOP_LEVEL = [
    "README.md",
    "CITATION.cff",
    "COMPLIANCE.md",
    "SECURITY.md",
    "LICENSE",
]

metadata_pat = re.compile(r"^---\s*(.*?)---", re.DOTALL)

issues = []

# --------------------------------------------------------------
# Validators
# --------------------------------------------------------------


def validate_metadata_block(path: pathlib.Path):
    text = path.read_text(encoding="utf-8", errors="ignore")

    m = metadata_pat.search(text)
    if not m:
        issues.append(f"[META] {path}: missing YAML metadata block.")
        return

    try:
        meta = yaml.safe_load(m.group(1))
    except Exception as e:
        issues.append(f"[META] {path}: invalid YAML metadata ({e}).")
        return

    # Required fields
    for key in REQUIRED_METADATA_FIELDS:
        if key not in meta:
            issues.append(f"[META] {path}: missing required field '{key}'.")

    # Filetype allowed?
    ft = meta.get("filetype")
    if ft and ft not in ALLOWED_FILETYPES:
        issues.append(f"[META] {path}: invalid filetype '{ft}'.")

    # DOI correctness
    doi = meta.get("doi")
    if doi and doi not in (CONCEPT_DOI, "(assigned upon publication)"):
        issues.append(f"[META] {path}: unexpected DOI '{doi}'.")

    return


def validate_DOIs(path: pathlib.Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in re.findall(r"10\.5281/zenodo\.\d+", text):
        if match != CONCEPT_DOI:
            issues.append(f"[DOI] {path}: found non-concept DOI '{match}'.")


def validate_ADR_references(path: pathlib.Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    adr_refs = re.findall(r"\bADR-(\d{4})\b", text)

    existing_adrs = {
        p.stem.split("-")[1]
        for p in (ROOT / "decisions").glob("ADR-*.md")
    }

    for adr in adr_refs:
        if adr not in existing_adrs:
            issues.append(f"[ADR] {path}: references ADR-{adr} which does not exist.")


def validate_required_top_level():
    for fname in REQUIRED_TOP_LEVEL:
        if not (ROOT / fname).exists():
            issues.append(f"[REQ] Missing required top-level file '{fname}'.")


# --------------------------------------------------------------
# MAIN SCAN
# --------------------------------------------------------------

validate_required_top_level()

for md in ROOT.rglob("*.md"):
    if "runs_legacy" in str(md):
        continue

    validate_metadata_block(md)
    validate_DOIs(md)
    validate_ADR_references(md)

# --------------------------------------------------------------
# REPORT
# --------------------------------------------------------------

if not issues:
    print("✅ Doc Guard: no issues found.")
    sys.exit(0)

print("⚠️ Doc Guard warnings:")
for msg in issues:
    print(" -", msg)

if STRICT:
    print("\n❌ DOC_GUARD_STRICT=1 → failing build due to issues.")
    sys.exit(1)
else:
    print("\n(Non-blocking) Set DOC_GUARD_STRICT=1 to fail on issues.")
    sys.exit(0)
