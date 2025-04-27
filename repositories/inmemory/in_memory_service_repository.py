from repositories.service_repository import ServiceRepository
from typing import Optional, List
from src.service import Service

class InMemoryServiceRepository(ServiceRepository):
    def __init__(self):
        self._storage = {}

    def save(self, service: Service) -> None:
        self._storage[service.service_id] = service

    def find_by_id(self, id: str) -> Optional[Service]:
        return self._storage.get(id)

    def find_all(self) -> List[Service]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
