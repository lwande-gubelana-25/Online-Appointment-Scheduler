# /repositories/repository.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')   # Entity Type
ID = TypeVar('ID') # ID Type

class Repository(ABC, Generic[T, ID]):

    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or update an entity."""
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Retrieve an entity by its ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Retrieve all entities."""
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete an entity by ID."""
        pass
