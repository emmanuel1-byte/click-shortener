from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from ..repositories import user_repository as repository
from ..utils.database import get_session
from ..schemas.user_schema import SignupSchema, LoginSchema
from ..helpers.token import create_access_token
import bcrypt

auth = APIRouter(prefix="/api/auth")


@auth.post("/signup", tags=["Authentication"])
def signup(
    signup_schema: SignupSchema, session: Annotated[Session, Depends(get_session)]
):

    existing_user = repository.find_user_by_email(signup_schema.email, session)
    if existing_user:
        raise HTTPException(status_code=409, detail="Account already exist")
    else:
        hashed_password = bcrypt.hashpw(
            signup_schema.password.encode("utf-8"), bcrypt.gensalt(rounds=12)
        ).decode("utf-8")

        new_user = repository.create_user(signup_schema, hashed_password, session)

        return JSONResponse(
            content={
                "data": {"user": new_user.model_dump(mode="json", exclude="password")}
            },
            status_code=201,
        )


@auth.post("/login", tags=["Authentication"])
async def login(
    login_schema: LoginSchema, session: Annotated[Session, Depends(get_session)]
):
    user = repository.find_user_by_email(login_schema.email, session)
    if not user:
        return JSONResponse(
            content={"message": "Account does not exist"}, status_code=404
        )

    compare_password = bcrypt.checkpw(
        login_schema.password.encode("utf-8"), user.password.encode("utf-8")
    )
    if not compare_password:
        return JSONResponse(content={"mesage": "Invalid credentials"}, status_code=401)

    accesss_token = create_access_token(user.id)

    return JSONResponse(
        content={
            "data": {
                "access_token": accesss_token,
                "user": user.model_dump(mode="json", exclude="password"),
            }
        }
    )
