import shlex

from models import BaseMessage, Unknown

from src.constants import MESSAGE_CLS_MAPPING

MESSAGE_TYPE_LOC = 0


def _resolver(message_type: str) -> BaseMessage:
    _message_cls = MESSAGE_CLS_MAPPING.get(message_type, Unknown)

    if _message_cls is None:
        raise ValueError(f"There is no {message_type} model.")

    return _message_cls


def parse_log(file_path: str):
    messages = []

    with open(file_path, encoding="utf-8") as log_file:
        for line in log_file:
            formatted_message = shlex.split(line)
            _, message_type = formatted_message[MESSAGE_TYPE_LOC].split("=")
            message_cls = _resolver(message_type)

            message = message_cls.from_list(formatted_message)

            messages.append(message)
    return messages
