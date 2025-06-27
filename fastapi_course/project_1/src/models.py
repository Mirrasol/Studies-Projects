from dataclasses import dataclass
from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field


def is_valid(message: str) -> str:
    invalid_terms = ["редиск", "бяк", "козявк"]
    for word in message.split():
        for term in invalid_terms:
            if word.startswith(term):
                raise ValueError("Использование недопустимых слов")
    return message


@dataclass
class User(BaseModel):
    name: str
    id: int | None = None
    age: int | None = None


@dataclass
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: Annotated[
        str,
        Field(min_length=10, max_length=500),
        AfterValidator(is_valid),
    ]
