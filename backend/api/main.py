from fastapi import APIRouter

from api.routes import ranker


api_router = APIRouter()
api_router.include_router(ranker.router, tags=["ranker"])
