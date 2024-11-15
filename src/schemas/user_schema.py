from pydantic import BaseModel, EmailStr, Field


class SignupSchema(BaseModel):
    fullname: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

    class Config:
        from_attributes = True
