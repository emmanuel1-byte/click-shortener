from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from uuid import uuid4


class URL(SQLModel, table=True):
    """
    SQLModel for storing URL shortening data with user relationship.
    """

    __tablename__ = "urls"

    # Primary Fields
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    original_url: str = Field(index=True)
    code: str = Field(unique=True, index=True)
    short_url: str = Field(unique=True)

    # Foreign Key and Relationship
    user_id: str = Field(foreign_key="users.id", ondelete="CASCADE")

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
        return f"URL(id={self.id}, code={self.code}, short_url={self.short_url})"
