from repositories.provider_repository import ProviderRepository
from typing import Optional, List
from src.provider import Provider

class InMemoryProviderRepository(ProviderRepository):
    def __init__(self):
        self._storage = {}

    def save(self, provider: Provider) -> None:
        self._storage[provider.provider_id] = provider

    def find_by_id(self, id: str) -> Optional[Provider]:
        return self._storage.get(id)

    def find_all(self) -> List[Provider]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
