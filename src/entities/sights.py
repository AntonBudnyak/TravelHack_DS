from typing import List

from pydantic import BaseModel


class SightsList(BaseModel):
    sight_ids: List[int]
    cities: str
