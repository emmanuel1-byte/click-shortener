from sqlmodel import Session, select
from ..models.analytics_model import Analytics
from ..models.url_model import URL


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

        return dict(new_analytics)


def get_url_analytics(url_id, session: Session):
    statement = select(Analytics).where(Analytics.url_id == url_id)
    result = session.exec(statement).fetchall()

    if result is None:
        return None
    else:
        return result
