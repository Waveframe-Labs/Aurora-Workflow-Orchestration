#!/usr/bin/env python3
"""
normalize_metadata.py — AWO Metadata Normalizer
------------------------------------------------
Scans the repository for markdown, text, and JSON files and ensures they
contain correct metadata blocks according to metadata_rules.json and
kernel/include.list.

This script:
  • Detects existing YAML-style metadata blocks at the top of files
  • Merges missing/default fields
  • Infers filetype based on directory rules
  • Applies forced awokernel flags via kernel/include.list
  • Updates timestamps
  • Writes updated files in-place

"""

import re
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

ROOT = Path(".").resolve()
RULES_PATH = ROOT / "metadata_rules.json"
INCLUDE_LIST = ROOT / "kernel/include.list"

# ---------------------------------------------------------------------
# Load rules
# ---------------------------------------------------------------------
with open(RULES_PATH, "r") as f:
    RULES = json.load(f)

DEFAULT_META = RULES["default_metadata"]
DIR_RULES = RULES["directory_rules"]

# ---------------------------------------------------------------------
# Load include list
# ---------------------------------------------------------------------
FORCE_INCLUDE = set()
if INCLUDE_LIST.exists():
    for line in INCLUDE_LIST.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            FORCE_INCLUDE.add(line)

# ---------------------------------------------------------------------
# Regex for detecting YAML metadata blocks
# ---------------------------------------------------------------------
META_REGEX = re.compile(
    r"^---\n(.*?)\n---\n",
    re.DOTALL
)

# ---------------------------------------------------------------------
# Helper to parse metadata block
# ---------------------------------------------------------------------
def parse_yaml_block(text: str) -> Dict[str, Any]:
    data = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip() or None
    return data

# ---------------------------------------------------------------------
# Helper to render YAML metadata block
# ---------------------------------------------------------------------
def render_yaml_block(meta: Dict[str, Any]) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            lines.append(f"{k}:")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"

# ---------------------------------------------------------------------
# Determine filetype by directory
# ---------------------------------------------------------------------
def infer_filetype(path: Path) -> str:
    parts = path.parts
    for folder, ftype in DIR_RULES.items():
        if folder in parts:
            return ftype
    return DEFAULT_META["filetype"]

# ---------------------------------------------------------------------
# Whether file should be kernel-included
# ---------------------------------------------------------------------
def should_force_kernel(path: Path) -> bool:
    rel = str(path).replace("\\", "/")
    return rel in FORCE_INCLUDE

# ---------------------------------------------------------------------
# Normalize a file
# ---------------------------------------------------------------------
def normalize_file(path: Path):
    text = path.read_text(encoding="utf-8")

    # Detect metadata
    match = META_REGEX.match(text)
    if match:
        meta_text = match.group(1)
        content = text[match.end():]
        meta = parse_yaml_block(meta_text)
    else:
        meta = {}
        content = text

    # Merge defaults
    for k, v in DEFAULT_META.items():
        meta.setdefault(k, v)

    # Infer filetype if missing
    meta["filetype"] = infer_filetype(path)

    # Forced kernel include
    if should_force_kernel(path):
        meta["awokernel"] = True

    # Update timestamps
    now = datetime.utcnow().isoformat() + "Z"
    if meta.get("created") in (None, "", "null"):
        meta["created"] = now
    meta["updated"] = now

    # Render new file
    new_text = render_yaml_block(meta) + content

    # Write back
    path.write_text(new_text, encoding="utf-8")
    print(f"[updated] {path}")

# ---------------------------------------------------------------------
# Walk repo
# ---------------------------------------------------------------------
TARGET_EXT = {".md", ".txt", ".json"}

for path in ROOT.rglob("*"):
    if path.suffix.lower() in TARGET_EXT and path.is_file():
        # skip in outputs or artifacts
        if "kernel/outputs" in str(path):
            continue
        if ".github" in path.parts and "workflows" in path.parts:
            continue
        normalize_file(path)

print("Metadata normalization complete.")
