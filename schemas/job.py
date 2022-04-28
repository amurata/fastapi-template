import datetime
from typing import List, Optional

from pydantic import BaseModel

from schemas.core import BaseSchema, PagingMeta


class JobResponse(BaseSchema):
    id: str
    title: str
    deleted_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class JobCreate(BaseSchema):
    title: str


class JobUpdate(BaseSchema):
    title: Optional[str] = None


class JobsPagedResponse(BaseSchema):
    data: Optional[List[JobResponse]]
    meta: Optional[PagingMeta]
