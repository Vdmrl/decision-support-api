import asyncio

from services.data_to_texts import UserData, SupportData

async def main():
    user_data = UserData()
    await user_data.account_to_texts(2)
    await user_data.event_to_texts(41)
    print(user_data.texts)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
