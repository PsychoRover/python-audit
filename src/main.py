import glob
import pathlib

from db import create_db_and_tables, engine
from loguru import logger
from sqlmodel import Session

from src.constants import DATABASE, LOG_GLOB_PATTERN
from src.log_parser import parse_log


def main():
    logger.debug(f"{'Initializing Database':*^50}")
    pathlib.Path(DATABASE).unlink(missing_ok=True)
    create_db_and_tables()

    logger.debug(f"{'Getting Auditd Logs':*^50}")
    logs = glob.glob(LOG_GLOB_PATTERN)

    logger.debug(f"{'Running Parser...':*^50}")
    for log in logs:
        messages = parse_log(log)
        with Session(engine) as session:
            session.add_all(messages)

            session.commit()


if __name__ == "__main__":
    main()
