from typing import Annotated
from ..utils.database import get_session
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlmodel import Session
from ..schemas.url_scheme import UrlSchema
from ..models.user_model import User
from ..repositories.url_repository import create_short_url, get_url, get_all_url
from ..repositories.analytics_repository import create_analytics
from ..helpers.authenticate_user import get_current_user
from nanoid import generate

url_shortner = APIRouter(prefix="/api/shorten-url")


@url_shortner.post("/", tags=["Shortener"])
def shorten_url(
    user_id: Annotated[User, Depends(get_current_user)],
    url_schema: UrlSchema,
    session: Annotated[Session, Depends(get_session)],
):
    code = generate(size=5)
    short_url = create_short_url(url_schema.long_url, user_id, code, session)
    return JSONResponse(content={"data": {"short_url": short_url}}, status_code=201)


@url_shortner.get("/{code}", tags=["Shortener"])
def redirect_to_original_url(
    session: Annotated[Session, Depends(get_session)],
    request: Request,
    code: str,
):
    shorten_url = get_url(code, session)
    if shorten_url is None:
        raise HTTPException(status_code=404, detail="Url does not exist")

    new_analytics = {"url_id": shorten_url.id, "ip_address": request.client.host}
    print(new_analytics, "Route....")
    create_analytics(new_analytics, session)

    return RedirectResponse(shorten_url.original_url, status_code=307)


@url_shortner.get("/", tags=["Shortener"])
def get_urls(
    session: Annotated[Session, Depends(get_session)],
    user_id: Annotated[User, Depends(get_current_user)],
):
    urls = get_all_url(user_id, session)
    return JSONResponse(content={"data": urls})
