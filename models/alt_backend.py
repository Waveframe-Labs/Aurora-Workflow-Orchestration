import hashlib, random
from .base import ModelBackend

class LocalUpper(ModelBackend):
    """
    Deterministic 'second model':
    - Uppercases prompt, adds a stable hash tail to mimic a different backend.
    """
    name = "upper-v1"

    def generate(self, prompt: str, *, params: dict) -> dict:
        seed = int(params.get("seed", 0))
        h = int(hashlib.sha256(("ALT::" + prompt).encode("utf-8")).hexdigest(), 16) % 10_000
        random.seed(seed + h)
        text = "[UPPER] " + prompt.strip().upper()
        return {"text": text, "usage": {}, "meta": {"model": self.name, **params}}
