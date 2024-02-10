from src.models.base import BaseMessage


class Cwd(BaseMessage, table=True):
    cwd: str
