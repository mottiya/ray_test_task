from abc import ABC, abstractmethod
from typing import List, Optional


class AbstractRepository(ABC):

    @abstractmethod
    def fetch_by_id(self, id: str) -> Optional[None]:
        raise NotImplementedError

    @abstractmethod
    def fetch_all(self) -> List[None]:
        raise NotImplementedError
    
    @abstractmethod
    def create_book(self, data: dict) -> Optional[None]:
        raise NotImplementedError

    @abstractmethod
    def update_book(self, book_id: str, data: dict) -> Optional[None]:
        raise NotImplementedError

    @abstractmethod
    def delete_book_by_id(self, book_id: str) -> None:
        raise NotImplementedError
