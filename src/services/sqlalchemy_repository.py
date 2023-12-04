from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, insert, select, update

from ..usecase.abs_repository import AbstractRepository

class SqlAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data:dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()
    
    async def find_all(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res
    
    async def update_one(self, data:dict, **filter_by):
        stmt = update(self.model).values(**data).filter_by(**filter_by).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()
    
    async def delete_one(self, id: str):
        stmt = delete(self.model).where(self.model.c.id == id)
        await self.session.execute(stmt)
