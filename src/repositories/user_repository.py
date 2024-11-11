from sqlmodel import select, Session
from ..models.user_model import User
from ..schemas.user_schema import SignupSchema


def find_user_by_email(email, session: Session):
    statement = select(User).where(User.email == email)
    result = session.exec(statement).first()
    return result


def get_user_by_id(user_id, session: Session):
    statement = select(User).where(User.id == user_id)
    result = session.exec(statement).first()
    return result


def create_user(data: SignupSchema, hashed_password, session: Session):
    data.password = hashed_password
    user = User(**data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def list_users(session: Session):
    statement = select(User)
    result = session.exec(statement).all()
    return result
