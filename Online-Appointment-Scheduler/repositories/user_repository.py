from abc import ABC, abstractmethod
from typing import Optional, List
from src.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User): pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]: pass

    @abstractmethod
    def find_all(self) -> List[User]: pass

    @abstractmethod
    def delete(self, user_id: str): pass
