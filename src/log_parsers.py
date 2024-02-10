from models.message_resolver import resolver

MESSAGE_TYPE_LOC = 0


REMOVE_ASSIGNMENT = r"\b\w+="


def parse_log(file_path: str):
    with open(file_path, encoding="utf-8") as log_file:
        for line in log_file:
            # Previous Implementation
            # formatted_message = re.sub(REMOVE_ASSIGNMENT, "", line)
            # message = formatted_message.split()
            # message_type = message[MESSAGE_TYPE_LOC]

            formatted_message = line.split()
            _, message_type = formatted_message[MESSAGE_TYPE_LOC].split("=")
            message_cls = resolver(message_type)

            message = message_cls.from_list(formatted_message)

            return message
