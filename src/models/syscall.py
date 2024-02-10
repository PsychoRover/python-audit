from models.base import BaseMessage


class SysCall(BaseMessage, table=True):
    arch: str
    syscall: str
    success: str
    exit: str
    a0: str
    a1: str
    a2: str
    a3: str
    items: str
    ppid: str
    pid: str
    auid: str
    uid: str
    gid: str
    euid: str
    suid: str
    fsuid: str
    egid: str
    sgid: str
    fsgid: str
    tty: str
    ses: str
    exe: str
    key: str
