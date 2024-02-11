import pathlib

from sqlmodel import SQLModel, create_engine

from src import logger
from src.constants import DATABASE

sqlite_url = f"sqlite:///{DATABASE}"

engine = create_engine(
    sqlite_url,
    echo=False,  # Set to True to automatically log DB actions.
)


@logger.catch()
def create_db_and_tables():
    logger.debug(f"{'Initializing Database':*^50}")
    pathlib.Path(DATABASE).unlink(missing_ok=True)
    SQLModel.metadata.create_all(engine)
