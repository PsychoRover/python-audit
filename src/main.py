from log_parsers import parse_log

from db import SQLModel, engine


def main():
    test = parse_log("src/auditd.log.1")

    SQLModel.metadata.create_all(engine)
    ...


if __name__ == "__main__":
    main()
