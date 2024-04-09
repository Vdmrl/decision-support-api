from typing import List

from pydantic import BaseModel


class SupportIds(BaseModel):
    support_ids: List[int]
