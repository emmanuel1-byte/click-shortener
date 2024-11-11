from sqlmodel import SQLModel, Field, Relationship
import uuid
from datetime import datetime, timezone
from pydantic import ConfigDict
from typing import List


def delayed_url_import():
    from .url_model import Url

    return Url


class User(SQLModel, table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    fullname: str
    email: str = Field(index=True, unique=True)
    password: str
    urls: List["Url"] = Relationship(back_populates="user", cascade_delete=True)
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: datetime = Field(default=datetime.now(timezone.utc))


@property
def url_model(self):
    delayed_url_import()
