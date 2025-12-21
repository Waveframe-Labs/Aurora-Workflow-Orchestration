import hashlib, random
from .base import ModelBackend

class LocalEcho(ModelBackend):
    name = "echo-v1"

    def generate(self, prompt: str, *, params: dict) -> dict:
        seed = int(params.get("seed", 0))
        # deterministic transform keyed by prompt+seed
        h = int(hashlib.sha256(prompt.encode("utf-8")).hexdigest(), 16) % 10_000
        random.seed(seed + h)
        text = "[ECHO] " + prompt.strip()
        return {"text": text, "usage": {}, "meta": {"model": self.name, **params}}
