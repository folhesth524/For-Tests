from attr.setters import validate
from pydantic import BaseModel, validator, field_validator
from src.enums.user_enums import Genders, UserErrors, Status


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Status

    @field_validator('email')
    @classmethod
    def check_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL_ADDRESS.value)



