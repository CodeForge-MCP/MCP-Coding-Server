# tools/base.py
from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def run(self, input_data: dict, language: str) -> dict:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass
