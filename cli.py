import sys
from awo.models.local_backend import LocalEcho
from awo.core.engine import run

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m awo.cli run <workflow.json>")
        sys.exit(2)

    cmd = sys.argv[1]
    if cmd == "run":
        workflow = sys.argv[2]
        backend = LocalEcho()
        run(workflow, backend)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(2)

if __name__ == "__main__":
    main()
