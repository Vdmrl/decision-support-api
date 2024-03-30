import os
import sys
import asyncio

from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload

from db.engine import session_factory, async_session_factory
from db.models.startup import Users

async def test_connection():
    # test sync connection
    with session_factory() as session:
        query = select(Users)
        result = session.execute(query)
        users = result.scalars().all()
        print(f"sync {users=}")

    # test async connection
    async with async_session_factory() as session:
        query = select(Users)
        result = await session.execute(query)
        users = result.scalars().all()
        print(f"async {users=}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_connection())

