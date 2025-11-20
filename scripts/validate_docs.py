#!/usr/bin/env python3
"""
Doc Guard — AWO/CRI-Compatible Documentation Validator
Non-blocking by default (DOC_GUARD_STRICT=1 enables failure mode)

Validates:
- YAML metadata blocks
- required fields (filetype, version, license, orcid, etc.)
- filetype correctness
- ADR existence
- DOI correctness
- required top-level documentation
- forbidden drift (untyped docs)
"""

import re, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]

# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------
CONCEPT_DOI = "10.5281/zenodo.17013612"
STRICT = (pathlib.os.environ.get("DOC_GUARD_STRICT", "0") == "1")

# Required fields in metadata blocks
REQUIRED_METADATA_FIELDS = [
    "filetype",
    "version",
    "license",
]

REQUIRED_TOP_LEVEL_FILES = [
    "README.md",
    "CITATION.cff",
    "COMPLIANCE.md",
    "SECURITY.md",
    "LICENSE",
]

ALLOWED_FILETYPES = {
    "doctrine",
    "specification",
    "documentation",
    "method_spec",
    "schema",
}

# -------------------------------------------------------------------
issues = []
metadata_pat = re.compile(r"^---\s*(.*?)---", re.DOTALL)


def scan_markdown_metadata(path: pathlib.Path):
    """Extract and validate the YAML metadata block from a file."""
    text = path.read_text(encoding="utf-8", errors="ignore")

    m = metadata_pat.search(text)
    if not m:
        issues.append(f"[META] {path}: missing YAML metadata block.")
        return

    raw_yaml = m.group(1)
    try:
        meta = yaml.safe_load(raw_yaml)
    except Exception as e:
        issues.append(f"[META] {path}: invalid YAML metadata ({e})")
        return

    # Required fields
    for key in REQUIRED_METADATA_FIELDS:
        if key not in meta:
            issues.append(f"[META] {path}: missing required metadata field '{key}'")

    # Filetype correctness
    ft = meta.get("filetype")
    if ft and ft not in ALLOWED_FILETYPES:
        issues.append(f"[META] {path}: invalid filetype '{ft}' (must be one of {sorted(ALLOWED_FILETYPES)})")

    # DOI correctness
    doi = meta.get("doi")
    if doi and doi != "(assigned upon publication)" and doi != CONCEPT_DOI:
        issues.append(f"[META] {path}: unexpected DOI {doi} (expected concept DOI or placeholder)")

    return


def validate_DOIs_in_text(path: pathlib.Path):
    """Warn about inconsistent DOIs inside content."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    doi_pat = re.compile(r"10\.5281/zenodo\.\d+")

    for m in doi_pat.finditer(text):
        if m.group(0) != CONCEPT_DOI:
            issues.append(f"[DOI] {path}: contains non-concept DOI '{m.group(0)}'")


def validate_ADR_references(path: pathlib.Path):
    """Ensure ADR references point to actual ADR files."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    adr_ref_pat = re.compile(r"\bADR-(\d{4})\b", re.IGNORECASE)

    existing_adrs = {
        p.stem.split("-")[1]
        for p in (ROOT / "decisions").glob("ADR-*.md")
    }

    for m in adr_ref_pat.finditer(text):
        adr = m.group(1)
        if adr not in existing_adrs:
            issues.append(f"[ADR] {path}: references non-existent ADR-{adr}")


def validate_required_files():
    """Ensure mandatory top-level files exist."""
    for fname in REQUIRED_TOP_LEVEL_FILES:
        if not (ROOT / fname).exists():
            issues.append(f"[REQ] Missing required top-level file: {fname}")


# -------------------------------------------------------------------
# MAIN SCAN
# -------------------------------------------------------------------
validate_required_files()

# Scan all Markdown files in repo
for md in ROOT.rglob("*.md"):
    if "runs_legacy" in str(md):
        continue
    scan_markdown_metadata(md)
    validate_DOIs_in_text(md)
    validate_ADR_references(md)

# -------------------------------------------------------------------
# REPORT
# -------------------------------------------------------------------
if not issues:
    print("✅ Doc Guard: no issues found.")
    sys.exit(0)

print("⚠️ Doc Guard warnings:")
for line in issues:
    print(" -", line)

if STRICT:
    print("\n❌ DOC_GUARD_STRICT=1 → failing due to issues.")
    sys.exit(1)
else:
    print("\n(Non-blocking) Set DOC_GUARD_STRICT=1 to enable blocking mode.")
    sys.exit(0)
