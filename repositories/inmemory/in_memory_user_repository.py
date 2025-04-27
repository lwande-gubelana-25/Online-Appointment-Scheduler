# /repositories/inmemory/in_memory_user_repository.py

from repositories.user_repository import UserRepository
from typing import Optional, List
from src.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage = {}  # Dictionary for storing users

    def save(self, user: User) -> None:
        self._storage[user.user_id] = user

    def find_by_id(self, id: str) -> Optional[User]:
        return self._storage.get(id)

    def find_all(self) -> List[User]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
