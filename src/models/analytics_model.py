from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from uuid import uuid4


class Analytics(SQLModel, table=True):
    """
    SQLModel for storing URL click analytics data.
    """

    __tablename__ = "analytics"

    # Primary Fields
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    ip_address: str

    # Foreign Key and Relationship
    url_id: str = Field(foreign_key="urls.id", ondelete="CASCADE")

    # Timestamp
    click_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self) -> str:
        return (
            f"Analytics(id={self.id}, url_id={self.url_id}, click_at={self.click_at})"
        )
