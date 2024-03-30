import asyncio

from services.userdata_to_texts import UserData

#async def test_connection():
#    # test sync connection
#    with session_factory() as session:
#        query = select(Users)
#        result = session.execute(query)
#        users = result.scalars().all()
#        print(f"sync {users=}")
#
#    # test async connection
#    async with async_session_factory() as session:
#        query = select(Users)
#        result = await session.execute(query)
#        users = result.scalars().all()
#        print(f"async {users=}")

if __name__ == "__main__":
    #asyncio.get_event_loop().run_until_complete(test_connection())
    user_data = UserData()
    asyncio.get_event_loop().run_until_complete(user_data.account_to_texts(2))
    print(user_data.texts)
