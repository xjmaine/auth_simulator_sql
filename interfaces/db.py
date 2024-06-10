from typing import Any
from abc import ABC, abstractmethod


class Database(ABC):
    """Database interface"""
    
    _file = None

    @abstractmethod
    def add(self, item: Any) -> None:
        """Add an item to the database"""
        pass

    @abstractmethod
    def update(self, id: str, item: Any) -> None:
        """Update an item in the database"""
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete an item from the database"""
        pass

    @abstractmethod
    def all(self) -> Any:
        """Return all items in the database"""
        pass

    @abstractmethod
    def get(self, item: Any) -> Any:
        """Get an item from the database"""
        pass


# I fix one of the issue wey I push, wey I dey pull request so go do the code review the merge am