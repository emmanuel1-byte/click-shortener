from fastapi import HTTPException, Depends
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError
import jwt
from sqlmodel import Session
from ..utils.database import get_session
from ..repositories.user_repository import get_user_by_id
from ..models.user_model import User
import os
import dotenv

dotenv.load_dotenv()

security = HTTPBearer()


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    session: Annotated[Session, Depends(get_session)],
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token.credentials, os.getenv("JWT_SECRET"), algorithms="HS256"
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = get_user_by_id(user_id, session)
    if user is None:
        raise credentials_exception
    return user.id
