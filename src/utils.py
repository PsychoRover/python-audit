import re


def sanitize_field_name(field_name: str):
    return re.sub(r"[\[\]]", "", field_name)
