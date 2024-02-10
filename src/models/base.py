from typing import Optional

from sqlmodel import Field, SQLModel

from src.utils import sanitize_field_name


class BaseMessage(SQLModel, extend_existing=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    msg: str

    @classmethod
    def from_list(cls, fields: list[str]):
        data = {}
        for field in fields:
            name, value = field.split("=")
            name = sanitize_field_name(name)
            data[name] = value

        return cls(**data)
