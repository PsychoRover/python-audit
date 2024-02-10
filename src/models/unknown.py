from models import BaseMessage

TYPE_AND_MSG_LOC = 2


class Unknown(BaseMessage, table=True):
    args: str

    @classmethod
    def from_list(cls, fields: list[str]) -> "Unknown":
        data = {"args": ", ".join(fields[TYPE_AND_MSG_LOC:])}

        for field in fields[:TYPE_AND_MSG_LOC]:
            name, value = field.split("=")
            data[name] = value

        return cls(**data)  # type: ignore
