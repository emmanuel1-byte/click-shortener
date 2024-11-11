from pydantic import BaseModel


class UrlSchema(BaseModel):
    long_url: str

    class Config:
        orm_mode = True
