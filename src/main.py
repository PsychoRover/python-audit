from db import create_db_and_tables, engine
from sqlmodel import Session

from src.log_parsers import parse_log


def main():
    sys_1 = parse_log("src/auditd.log.1")
    create_db_and_tables()
    with Session(engine) as session:
        session.add(sys_1)

        session.commit()


if __name__ == "__main__":
    main()
