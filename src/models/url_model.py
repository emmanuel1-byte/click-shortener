from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from pydantic import ConfigDict
from .user_model import User
import uuid


def delayed_user_import():
    from .user_model import User

    return User


class Url(SQLModel, table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    original_url: str
    user_id: str = Field(foreign_key="user.id", ondelete="CASCADE")
    user: User = Relationship(back_populates="urls")
    code: str
    short_url: str
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: datetime = Field(default=datetime.now(timezone.utc))


@property
def user_model(self):
    delayed_user_import()
