from typing import List

from httpx import AsyncClient

from schemas.ranker import SupportIds
from services.data2text import SupportData


async def test_nonexistent_index(ac: AsyncClient):
    responce = await ac.get("/get_ranked_support_ids", params={"project_id": 999999999999})
    assert responce.status_code == 404


async def test_existent_index(ac: AsyncClient):
    responce = await ac.get("/get_ranked_support_ids", params={"project_id": 41})
    assert responce.status_code == 200
    assert len(responce.json()["support_ids"]) == len(await SupportData.get_all_texts())
