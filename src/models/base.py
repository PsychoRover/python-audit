from typing import Optional

from sqlmodel import Field, SQLModel


class BaseMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    msg: str

    @classmethod
    def from_list(cls, fields: list[str]):
        data = {}
        for field in fields:
            name, value = field.split("=")
            data[name] = value

        return cls(**data)
