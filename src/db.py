from sqlmodel import SQLModel, create_engine

from src.constants import DATABASE

sqlite_url = f"sqlite:///{DATABASE}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
