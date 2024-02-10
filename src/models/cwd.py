from models import BaseMessage


class Cwd(BaseMessage, table=True):
    cwd: str
