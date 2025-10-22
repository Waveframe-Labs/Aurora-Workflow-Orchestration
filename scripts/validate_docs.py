#!/usr/bin/env python3
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

# Files to scan (extend if needed)
FILES = [
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
]

# Directories for ADR existence check
DECISIONS_DIR = ROOT / "decisions"

# Policy knobs
CONCEPT_DOI = "10.5281/zenodo.17013612"
STRICT = (pathlib.os.environ.get("DOC_GUARD_STRICT", "0") == "1")

doi_pat = re.compile(r"10\.5281/zenodo\.\d+")
adr_ref_pat = re.compile(r"\bADR-(\d{4})\b", re.IGNORECASE)

issues = []

# 1) Enforce concept DOI only (warn on any other DOI)
for f in FILES:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8", errors="ignore")
    for m in doi_pat.finditer(text):
        found = m.group(0)
        if found != CONCEPT_DOI:
            issues.append(f"[DOI] {f.name}: found non-concept DOI '{found}' (use {CONCEPT_DOI})")

# 2) Ensure referenced ADRs actually exist
existing_adrs = set()
if DECISIONS_DIR.exists():
    for p in DECISIONS_DIR.glob("ADR-*.md"):
        m = re.search(r"ADR-(\d{4})", p.name, re.IGNORECASE)
        if m:
            existing_adrs.add(m.group(1))

for f in FILES:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8", errors="ignore")
    for m in adr_ref_pat.finditer(text):
        adr_num = m.group(1)
        if adr_num not in existing_adrs:
            issues.append(f"[ADR] {f.name}: references ADR-{adr_num} which does not exist under /decisions")

# Report
if not issues:
    print("✅ Doc Guard: no issues found.")
    sys.exit(0)

print("⚠️ Doc Guard warnings:")
for line in issues:
    print(" -", line)

# Non-blocking by default; fail only in strict mode
if STRICT:
    print("\n❌ DOC_GUARD_STRICT=1 -> failing build due to issues above.")
    sys.exit(1)
else:
    print("\n(Non-blocking) Set DOC_GUARD_STRICT=1 to fail on issues.")
    sys.exit(0)
