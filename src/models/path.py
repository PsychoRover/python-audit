from src.models.base import BaseMessage


class Path(BaseMessage, table=True):
    item: str
    name: str
    inode: str
    dev: str
    mode: str
    ouid: str
    ogid: str
    rdev: str
    nametype: str
    cap_fp: str
    cap_fi: str
    cap_fe: str
    cap_fver: str