from db import create_db_and_tables, engine
from log_parsers import parse_log
from sqlmodel import Session
from models import SysCall


def main():
    # sys_1 = parse_log("src/auditd.log.1")
    data = {
  "type": "SYSCALL",
  "msg": "audit(1600000000.000:123456)",
  "arch": "c000003e",
  "syscall": "2",
  "success": "yes",
  "exit": "0",
  "a0": "7ffeed0f5bff",
  "a1": "0",
  "a2": "1b6",
  "a3": "1b6",
  "items": "1",
  "ppid": "1234",
  "pid": "5678",
  "auid": "1000",
  "uid": "1000",
  "gid": "1000",
  "euid": "1000",
  "suid": "1000",
  "fsuid": "1000",
  "egid": "1000",
  "sgid": "1000",
  "fsgid": "1000",
  "tty": "(none)",
  "ses": "1",
  "comm": "cat",
  "exe": "/bin/cat",
  "key": "test"
}
    sys_1 = SysCall(**data)
    create_db_and_tables()
    with Session(engine) as session:
        session.add(sys_1)

        session.commit()


if __name__ == "__main__":
    main()
