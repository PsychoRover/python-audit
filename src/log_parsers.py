from models import BaseMessage, SysCall

MESSAGE_TYPE_LOC = 0


def _resolver(message_type: str) -> "BaseMessage":
    _message_cls = {
        "SYSCALL": SysCall,
    }.get(message_type)

    if _message_cls is None:
        raise ValueError(f"There is no {message_type} model.")

    return _message_cls


def parse_log(file_path: str):
    with open(file_path, encoding="utf-8") as log_file:
        for line in log_file:
            formatted_message = line.split()
            _, message_type = formatted_message[MESSAGE_TYPE_LOC].split("=")
            message_cls = _resolver(message_type)

            message = message_cls.from_list(formatted_message)

            return message
