from dotenv import load_dotenv

load_dotenv()
import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.exc import OperationalError


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    try:
        with Session(engine) as session:
            yield session
        print("Database connection succesfull")
    except OperationalError as e:
        print(f"Database connection failed: {e}")


