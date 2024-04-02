import asyncio

from services.data2text import ProjectData, SupportData
from services.text_ranker import ProjectRanker


async def main():
    ranker = ProjectRanker()
    ranker.bind_to(SupportData.get_all_texts)

    project_data = ProjectData()
    await project_data.accounts_to_texts(41)
    await project_data.project_data_to_texts(41)
    await project_data.project_passport_to_texts(41)
    await project_data.event_to_texts(41)
    sorted_indexes = await ranker.sort_for(await project_data.get_text())
    print(await project_data.get_text())
    texts = await SupportData.get_all_texts()
    for i in sorted_indexes:
        print(texts[i])


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
