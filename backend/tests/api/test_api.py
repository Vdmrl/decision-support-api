from httpx import AsyncClient

from repositories.data2text import SupportData


async def test_nonexistent_index(client: AsyncClient):
    response = await client.get("/get_ranked_support_ids", params={"project_id": 999999999999})
    assert response.status_code == 404


async def test_existent_index(client: AsyncClient):
    response = await client.get("/get_ranked_support_ids", params={"project_id": 41})
    assert response.status_code == 200
    assert len(response.json()["support_ids"]) == len(await SupportData.get_all_texts())
