from pydantic import BaseModel


class UrlSchema(BaseModel):
    long_url: str

    class Config:
        from_attributes = True
