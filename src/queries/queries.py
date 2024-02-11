from collections import Counter

from models import Cwd
from queries.enums import By
from queries.str_queries import DISTINCT_COMMANDS
from sqlalchemy import text
from sqlmodel import Session, select

from src import logger
from src.constants import MESSAGE_CLS_MAPPING
from src.db import engine


def distinct_commands():
    with Session(engine) as session:
        rows = session.execute(text(DISTINCT_COMMANDS)).all()
        distinct_commands = [row.t[0] for row in rows]  # Ugly thing

    logger.info(f"Number of distinct commands {distinct_commands}")


def commands_count():
    with Session(engine) as session:
        rows = []
        for command in MESSAGE_CLS_MAPPING.values():
            statement = select(command)
            result = session.exec(statement).all()
            rows.append((len(result), command))

    logger.info(f"The most common command is: {max(rows, key=lambda x: x[0])}")
    logger.info(f"The least common command is: {min(rows, key=lambda x: x[0])}")


def executions_count(by: By = By.UID):
    """
    Logs the executions' number by a given id filed, e.g., 'uid', 'guid', etc.
    Use `By` string enum for easy access.
    """
    rows = []
    relevant_commands = [command for command in MESSAGE_CLS_MAPPING.values() if hasattr(command, by)]

    if not relevant_commands:
        logger.debug(f"No relevant command/s with {by} field is found")
        return

    with Session(engine) as session:
        for command_ in relevant_commands:
            statement = select(command_)
            result = session.exec(statement).all()
            rows.extend(result)

    counter = Counter([row.uid for row in rows])
    uid = max(counter, key=counter.get)  # type: ignore
    logger.info(f"User with {uid=} have done {counter[uid]} commands")


def folder_activity():
    with Session(engine) as session:
        statement = select(Cwd)
        result = session.exec(statement).all()

    counter = Counter([r.cwd for r in result])
    path = max(counter, key=counter.get)  # type: ignore
    logger.info(f"Most active {path=} with {counter[path]} commands")
