from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):

    @abstractmethod
    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def health_check(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass