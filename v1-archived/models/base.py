from typing import Dict, Any

class ModelBackend:
    name: str = "base"

    def generate(self, prompt: str, *, params: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
