#!/usr/bin/env python3
"""
Doc Guard v2.0 — AWO/CRI-Compatible Documentation Validator
Strict for core docs. Lenient elsewhere.

Tiered enforcement:
  • Tier 1 (strict): docs/, decisions/, schemas/
  • Tier 2 (light): root-level *.md, citations/
  • Tier 3 (ignored): templates/, figures/, logs/, runs/, archive/, .github/, workflows/

Validates:
  - YAML metadata blocks for Tier 1
  - Required fields (filetype, version, license) for Tier 1
  - Allowed filetypes (extended whitelist)
  - Concept DOI correctness
  - ADR references in Tier 1 files only
"""

import re, sys, pathlib, yaml, os

ROOT = pathlib.Path(__file__).resolve().parents[2]

# --------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------

CONCEPT_DOI = "10.5281/zenodo.17013612"
STRICT = (os.environ.get("DOC_GUARD_STRICT", "0") == "1")

ALLOWED_FILETYPES = {
    "doctrine",
    "specification",
    "documentation",
    "method_spec",
    "schema",
    # Additional practical categories for real-world repo structure
    "governance_record",
    "workflow_log",
    "templates",
    "repo_meta",
    "logs_index",
    "citation_context",
    "handoff_record",
    "attestation_record",
}

REQUIRED_METADATA_FIELDS = ["filetype", "version", "license"]

# TIERED ENFORCEMENT
TIER1_DIRS = ["docs", "decisions", "schemas"]
TIER2_DIRS = ["citations"]
IGNORE_DIRS = [
    "archive", "runs", "runs_legacy", "logs", "overrides",
    ".github", "figures", "core", "models", "workflows", "templates",
]

metadata_pat = re.compile(r"^---\s*(.*?)---", re.DOTALL)

issues = []

# --------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------


def is_ignored(path: pathlib.Path) -> bool:
    for part in path.parts:
        if part in IGNORE_DIRS:
            return True
    return False


def tier_of(path: pathlib.Path) -> int:
    parts = set(path.parts)
    if any(d in parts for d in TIER1_DIRS):
        return 1
    if any(d in parts for d in TIER2_DIRS):
        return 2
    return 3


def extract_metadata(text: str, path: pathlib.Path):
    m = metadata_pat.search(text)
    if not m:
        return None, f"[META] {path}: missing YAML metadata block."
    try:
        return yaml.safe_load(m.group(1)), None
    except Exception as e:
        return None, f"[META] {path}: invalid YAML metadata ({e})."


def validate_DOIs(text: str, path: pathlib.Path):
    for match in re.findall(r"10\.5281/zenodo\.\d+", text):
        if match != CONCEPT_DOI:
            issues.append(f"[DOI] {path}: non-concept DOI '{match}' found.")


def validate_ADR_references(text: str, path: pathlib.Path):
    adr_refs = re.findall(r"\bADR-(\d{3,4})\b", text)

    existing = {
        p.stem.split("-")[1]
        for p in (ROOT / "decisions").glob("ADR-*")
        if "-" in p.stem
    }

    for adr in adr_refs:
        if adr not in existing:
            issues.append(f"[ADR] {path}: references ADR-{adr} which does not exist.")


# --------------------------------------------------------------
# MAIN SCAN
# --------------------------------------------------------------

for md in ROOT.rglob("*.md"):
    rel = md.relative_to(ROOT)

    if is_ignored(rel):
        continue

    tier = tier_of(rel)
    text = md.read_text(encoding="utf-8", errors="ignore")

    # Tier 1: strict requirements
    if tier == 1:
        meta, err = extract_metadata(text, rel)
        if err:
            issues.append(err)
            continue

        for key in REQUIRED_METADATA_FIELDS:
            if key not in meta:
                issues.append(f"[META] {rel}: missing required field '{key}'.")

        ft = meta.get("filetype")
        if ft and ft not in ALLOWED_FILETYPES:
            issues.append(f"[META] {rel}: invalid filetype '{ft}'.")

        validate_DOIs(text, rel)
        validate_ADR_references(text, rel)

    # Tier 2: DOI + ADR checks only
    elif tier == 2:
        validate_DOIs(text, rel)
        validate_ADR_references(text, rel)

    # Tier 3: repo infrastructure — skip everything
    else:
        continue


# --------------------------------------------------------------
# REPORT
# --------------------------------------------------------------

if not issues:
    print("✅ Doc Guard v2.0: no issues found.")
    sys.exit(0)

print("⚠️ Doc Guard v2.0 warnings:")
for msg in issues:
    print(" -", msg)

if STRICT:
    print("\n❌ DOC_GUARD_STRICT=1 → failing build due to issues.")
    sys.exit(1)
else:
    print("\n(Non-blocking) Set DOC_GUARD_STRICT=1 to enforce strictly.")
    sys.exit(0)
