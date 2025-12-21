# awo/__init__.py
"""
Aurora Workflow Orchestration (AWO)
Lightweight, auditable execution primitives for the AWO method.
"""

# Semantic version of the Python package layer (not the repo release tag).
__version__ = "1.1.1"

# Small convenience re-exports so users can do:
#   from awo import run, LocalEcho
from .core.engine import run
from .core.lockfile import snapshot
from .models.local_backend import LocalEcho

__all__ = [
    "__version__",
    "run",
    "snapshot",
    "LocalEcho",
]
