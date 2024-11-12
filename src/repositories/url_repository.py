from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from ..models.url_model import URL
from ..models.user_model import User
import dotenv

dotenv.load_dotenv()
import os


def create_short_url(long_url, user_id, code, session: Session):
    short_url = URL(
        user_id=user_id,
        code=code,
        original_url=long_url,
        short_url=f"{os.getenv("HOST_NAME")}/{code}",
    )
    session.add(short_url)
    session.commit()
    session.refresh(short_url)
    short_url_dict = short_url.model_dump()

    short_url_dict["created_at"] = short_url.created_at.isoformat()
    short_url_dict["updated_at"] = short_url.updated_at.isoformat()

    return short_url_dict


def get_url(code, session: Session):
    statement = select(URL).where(URL.code == code)
    result = session.exec(statement).first()
    return result


def get_all_url(user_id, session: Session):
    statement = select(URL, User).join(User).where(URL.user_id == user_id)
    result = session.exec(statement)
    records = result.fetchall()

    # convert each record to dictionary format

    serialized_data = [
        {
            "url": jsonable_encoder(url),
            "user": jsonable_encoder(user, exclude=["password"]),
        }
        for url, user in records
    ]

    return serialized_data
