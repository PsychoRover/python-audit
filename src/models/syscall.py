from sqlmodel import SQLModel


class SysCall(SQLModel):
    arch: str
    syscall: int
    success: str
    exit: int
    a0: str
    a1: str
    a2: str
    a3: str
    items: int
    ppid: int
    pid: int
    auid: int
    uid: int
    gid: int
    euid: int
    suid: int
    fsuid: int
    egid: int
    sgid: int
    fsgid: int
    tty: str
    ses: int
    exe: str
    subj: str
    key: str

    @classmethod
    def from_list(cls, fields: list[str]):
        data = {}
        for field in fields:
            name, value = field.split("=")
            data[name] = value

        return cls(**data)
