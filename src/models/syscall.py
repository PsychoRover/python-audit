from typing import Optional

from models import BaseMessage


class SysCall(BaseMessage, table=True):
    arch: str
    syscall: str
    success: str
    exit: str
    a0: Optional[str]
    a1: Optional[str]
    a2: Optional[str]
    a3: Optional[str]
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
