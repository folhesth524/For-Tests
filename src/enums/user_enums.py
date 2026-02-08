from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'

class Status(Enum):
    inactive = 'inactive'
    active = 'active'

class UserErrors(Enum):
    WRONG_EMAIL_ADDRESS = 'Wrong email address'

