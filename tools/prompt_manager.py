# tools/prompt_manager.py
from typing import Dict, Any, List, Optional
import uuid

class PromptManager:
    """
    Simple in-memory prompt manager.
    Stores prompts with structure:
    {
      "id": "<uuid>",
      "name": "short name",
      "tool": "code_generation" or "code_review" or "code_refactor",
      "language": "python",
      "template": "Write a function that {task}..."
    }
    """
    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def create_prompt(self, name: str, tool: str, language: str, template: str) -> Dict[str, Any]:
        pid = str(uuid.uuid4())
        item = {"id": pid, "name": name, "tool": tool, "language": language, "template": template}
        self._store[pid] = item
        return item

    def list_prompts(self) -> List[Dict[str, Any]]:
        return list(self._store.values())

    def get_prompt(self, pid: str) -> Optional[Dict[str, Any]]:
        return self._store.get(pid)

    def update_prompt(self, pid: str, **kwargs) -> Optional[Dict[str, Any]]:
        if pid not in self._store:
            return None
    # Only allow certain keys
        allowed = {"name", "tool", "language", "template"}
        for k, v in kwargs.items():
            if k in allowed:
                self._store[pid][k] = v
        return self._store[pid]

    def delete_prompt(self, pid: str) -> bool:
        return self._store.pop(pid, None) is not None

# Singleton instance
manager = PromptManager()
