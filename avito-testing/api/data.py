from decimal import Decimal
from typing import List

from pydantic import BaseModel, field_validator

# from typing_extensions import Annotated
from api.validation import validate_fixed_length

# PhotosList = Annotated[List[str], BeforeValidator(validate_with_fixed_length(3))]


class CreateAdvertismentDTO(BaseModel):
    name: str
    description: str
    price: Decimal
    price: float
    photos: str

    @field_validator('photos')
    @classmethod
    def validate_fixed_length(cls, v):
        v = v.split(', ')
        
        assert validate_fixed_length(3)(v), \
        "Max number should be 3"

        return ', '.join(v)
