from typing import TYPE_CHECKING

from . import SysCall

if TYPE_CHECKING:
    from src.models.base import BaseMessage


def resolver(message_type: str) -> "BaseMessage":
    _message_cls = {
        "SYSCALL": SysCall,
    }.get(message_type)

    if _message_cls is None:
        raise ValueError(f"There is no {message_type} model.")

    return _message_cls
