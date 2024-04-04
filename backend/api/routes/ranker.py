from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from typing import List

from services.data2text import ProjectData, SupportData
from services.text_ranker import ProjectRanker

router = APIRouter()
ranker = ProjectRanker("all-MiniLM-L6-v2")  # create project ranker with "all-MiniLM-L6-v2" model


@router.on_event("startup")
async def startup_event():
    ranker.bind_to(SupportData.get_all_texts)  # bind ranker to get all supports texts function


@router.get("/get_ranked_support_ids",
            summary="return ranked ids of supports according to project id",
            status_code=status.HTTP_200_OK,
            response_model=List[int])
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

    return sorted_indexes
