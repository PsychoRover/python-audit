import glob
import pathlib

from db import create_db_and_tables, engine
from sqlmodel import Session

from src.constants import DATABASE, LOG_GLOB_PATTERN
from src.log_parser import parse_log


def main():
    pathlib.Path(DATABASE).unlink(missing_ok=True)
    create_db_and_tables()

    logs = glob.glob(LOG_GLOB_PATTERN)

    for log in logs:
        messages = parse_log(log)
        with Session(engine) as session:
            session.add_all(messages)

            session.commit()


if __name__ == "__main__":
    main()
