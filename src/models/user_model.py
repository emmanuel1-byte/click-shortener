from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from uuid import uuid4


class User(SQLModel, table=True):
    """
    SQLModel for user management with related shortened URLs.
    """

    __tablename__ = "users"

    # Primary Fields
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    fullname: str
    email: str = Field(index=True, unique=True)
    password: str

    # Timestamps
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email}, fullname={self.fullname})"
