from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from schemas.ranker import SupportIds
from repositories.data2text import ProjectData, SupportData
from services.text_ranker import ProjectRanker

from logger import logger


router = APIRouter()
ranker = ProjectRanker("all-MiniLM-L6-v2")  # create project ranker with "all-MiniLM-L6-v2" model
ranker.bind_to(SupportData.get_all_texts)  # bind ranker to get all supports texts function


@router.get(
    "/get_ranked_support_ids",
    summary="return ranked ids of supports according to project id",
    status_code=status.HTTP_200_OK,
    response_model=SupportIds,
)
@cache(expire=3600)  # 1 hour cache
async def get_ranked_support_ids(project_id: int):
    if not await ProjectData.is_in_db(project_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # get text for project
    project_data = ProjectData()
    await project_data.accounts_to_texts(project_id)
    await project_data.project_data_to_texts(project_id)
    await project_data.project_passport_to_texts(project_id)
    await project_data.event_to_texts(project_id)
    project_text = await project_data.get_text()

    # sort
    sorted_indexes = await ranker.sort_for(project_text)

    logger.info("supports ranked successfully", exc_info={
        "project_id": project_id,
        "project_text": project_text,
        "sorted_indexes": sorted_indexes,
    })

    return SupportIds(support_ids=sorted_indexes)


@router.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
