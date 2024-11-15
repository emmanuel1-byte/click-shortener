from sqlmodel import Session, select
from sqlalchemy import func
from ..models.analytics_model import Analytics
from ..models.url_model import URL
from fastapi.encoders import jsonable_encoder


def create_analytics(data: dict, session: Session):
    statement = select(URL).where(URL.id == data.get("url_id"))
    result = session.exec(statement).first()
    if result is None:
        return None
    else:
        new_analytics = Analytics(**data)
        session.add(new_analytics)
        session.commit()
        session.refresh(new_analytics)

        return jsonable_encoder(new_analytics)


def get_url_analytics(url_id, offset, limit, session: Session):
    statement = (
        select(Analytics)
        .where(Analytics.url_id == url_id)
        .offset((offset - 1) * limit)
        .limit(limit)
    )
    count = session.exec(
        select(func.count(Analytics.id)).where(Analytics.url_id == url_id)
    ).one()
    result = session.exec(statement).fetchall()

    if result is None:
        return None

    return (
        {
            "analytics": jsonable_encoder(result),
            "total_count": count,
            "offset": offset,
            "limit": limit,
        },
    )
