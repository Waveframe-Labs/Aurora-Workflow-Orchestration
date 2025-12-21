# awo/cli.py

import sys
import argparse
from pathlib import Path

from awo.models.local_backend import LocalEcho
from awo.core.engine import run as run_workflow

# If you set __version__ in awo/__init__.py this will show in --version
try:
    from awo import __version__
except Exception:
    __version__ = "1.1.1"

def _parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="python -m awo.cli",
        description="Aurora Workflow Orchestration (AWO) command-line interface",
    )
    p.add_argument("--version", action="version", version=f"AWO {__version__}")

    sub = p.add_subparsers(dest="cmd", required=True)

    # awo run <workflow.json> [--backend local]
    prun = sub.add_parser("run", help="Execute a workflow JSON file")
    prun.add_argument("workflow", help="Path to a workflow JSON (e.g., workflows/multimodel.json)")
    prun.add_argument(
        "--backend",
        default="local",
        choices=["local"],
        help="Model backend to use (default: local echo backend)",
    )
    return p.parse_args(argv)

def _make_backend(name: str):
    # Placeholder for future backends; today we keep LocalEcho.
    if name == "local":
        return LocalEcho()
    raise ValueError(f"Unsupported backend: {name!r}")

def main(argv=None):
    args = _parse_args(argv)

    if args.cmd == "run":
        wf_path = Path(args.workflow)
        if not wf_path.exists():
            print(f"[AWO] Workflow not found: {wf_path}", file=sys.stderr)
            return 2

        backend = _make_backend(args.backend)

        try:
            run_dir = run_workflow(str(wf_path), backend=backend)
            # If engine returns normally (no audit gate), confirm success:
            print(f"[AWO] Run completed.\n[AWO] Artifacts: {run_dir}")
            return 0

        except SystemExit as e:
            # Engine intentionally pauses at audit gate with exit code 78
            code = int(e.code) if isinstance(e.code, int) else 1
            if code == 78:
                print(
                    "[AWO] Audit gate reached — run paused for human approval.\n"
                    "      See report.md and gate_decision.yml in the run directory.",
                    file=sys.stderr,
                )
            return code

        except Exception as e:
            print(f"[AWO] Run failed: {e}", file=sys.stderr)
            return 1

    # Shouldn’t reach here because subparser requires a command
    return 2

if __name__ == "__main__":
    sys.exit(main())
