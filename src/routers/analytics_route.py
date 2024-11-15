from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
from sqlmodel import Session
from ..models.user_model import User
from ..helpers.authenticate_user import get_current_user
from ..utils.database import get_session
from ..repositories.analytics_repository import get_url_analytics

analytics = APIRouter(prefix="/api/analytics")


@analytics.get("/{url_id}", tags=["Analytics"])
def get_analytics(
    url_id: str,
    session: Annotated[Session, Depends(get_session)],
    user_id: Annotated[User, Depends(get_current_user)],
    offset: int = 1,
    limit: int = 10,
):
    analytics = get_url_analytics(url_id, offset, limit, session)
    if analytics is None:
        raise HTTPException(status_code=404, detail={"message": "URL not found"})
    return JSONResponse(content={"data": analytics}, status_code=200)
