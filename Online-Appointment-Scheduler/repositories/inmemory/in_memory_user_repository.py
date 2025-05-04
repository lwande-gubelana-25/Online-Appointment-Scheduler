from repositories.user_repository import UserRepository
from src.user import User
from typing import Dict, Optional, List

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.storage: Dict[str, User] = {}

    def save(self, user: User):
        self.storage[user.id] = user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self.storage.get(user_id)

    def find_all(self) -> List[User]:
        return list(self.storage.values())

    def delete(self, user_id: str):
        if user_id in self.storage:
            del self.storage[user_id]
