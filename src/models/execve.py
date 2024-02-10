from models import BaseMessage


class ExecVe(BaseMessage, table=True):
    argc: str
    argv0: str
    argv1: str
