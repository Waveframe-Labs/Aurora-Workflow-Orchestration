#!/usr/bin/env python3
import json, sys, pathlib

def die(msg, code=2):
    print(f"::error::{msg}")
    sys.exit(code)

def load_json(p: pathlib.Path):
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        die(f"Failed to read {p}: {e}")

def main():
    if len(sys.argv) != 2:
        die("Usage: validate_run.py <RUN_DIR>")
    run_dir = pathlib.Path(sys.argv[1]).resolve()
    schemas = pathlib.Path("schemas").resolve()
    if not run_dir.exists():
        die(f"Run dir not found: {run_dir}")

    try:
        from jsonschema import Draft202012Validator as Validator
    except Exception:
        die("jsonschema not installed. Add 'pip install jsonschema' before running.")

    man = load_json(run_dir / "run_manifest.json")
    prov = load_json(run_dir / "provenance.json")
    man_schema = load_json(schemas / "run_manifest.schema.json")
    prov_schema = load_json(schemas / "provenance.schema.json")

    # Validate manifest
    Validator(man_schema).validate(man)

    # Validate provenance (list of records)
    if not isinstance(prov, list):
        die("provenance.json must be a list")

    for i, rec in enumerate(prov):
        try:
            Validator(prov_schema).validate(rec)
        except Exception as e:
            die(f"Provenance record {i} invalid: {e}")

    print("Schema validation OK")

if __name__ == "__main__":
    main()
