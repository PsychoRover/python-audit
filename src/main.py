import glob

from db import create_db_and_tables, engine
from queries.queries import commands_count, distinct_commands, executions_count, folder_activity
from sqlmodel import Session

from src import logger
from src.constants import LOG_GLOB_PATTERN
from src.log_parser import parse_log


def main():
    create_db_and_tables()

    logger.debug(f"{'Getting Auditd Logs':*^50}")
    logs = glob.glob(LOG_GLOB_PATTERN)  # In a real world application this would be a folder Watcher!

    logger.debug(f"{'Running Parser...':*^50}")
    for log in logs:
        messages = parse_log(log)
        with Session(engine) as session:
            session.add_all(messages)

            session.commit()

    logger.debug(f"{'Running Queries...':*^50}")
    distinct_commands()
    commands_count()
    executions_count()
    folder_activity()


if __name__ == "__main__":
    main()
