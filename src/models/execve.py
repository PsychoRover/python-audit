from typing import Optional

from models import BaseMessage


class ExecVe(BaseMessage, table=True):
    argc: str
    a0: Optional[str]
    a1: Optional[str]
    a2: Optional[str]
    a3: Optional[str]
