from models import BaseMessage


class ProcTitle(BaseMessage, table=True):
    proctitle: str
