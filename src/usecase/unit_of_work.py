from abc import ABC, abstractmethod
from typing import Any, Callable

from .abs_repository import AbstractRepository

# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
class IUnitOfWork(ABC):
    
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self, session_factory: Callable[..., Any], repository: AbstractRepository):
        self.session_factory = session_factory
        self.repository = repository(self.session_factory)

    async def __aenter__(self):
        self.session = self.session_factory()

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()