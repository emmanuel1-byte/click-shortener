from sqlmodel import Session, select
from ..models.url_model import Url
import dotenv

dotenv.load_dotenv()
import os


def create_short_url(long_url, user_id, code, session: Session):
    print(os.getenv("HOST_NAME"), "MIX....")
    short_url = Url(
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
    statement = select(Url).where(Url.code == code)
    result = session.exec(statement).first()
    return result
