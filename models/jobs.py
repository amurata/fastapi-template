from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text, func
from sqlalchemy.sql.functions import current_timestamp

from core.database import Base
from core.utils import get_ulid

from . import ModelBase


class Job(Base, ModelBase):

    __tablename__ = "jobs"
    mysql_charset = ("utf8mb4",)
    mysql_collate = "utf8mb4_unicode_ci"

    title = Column(String(100))
    description = Column(Text)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=current_timestamp(),
        onupdate=func.utc_timestamp(),
    )
