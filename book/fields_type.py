from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List

from utils.validation_email import validation_email
from utils.validation_phone import validation_phone


@dataclass
class Field:
    value: str


@dataclass
class Name(Field):
    value: str
    # make formating name for removing all whitespaces and store it as title

@dataclass
class Phone(Field):
    value: str

    def __post_init__(self):
        pass # make validation_phone(self.value)

@dataclass
class Birthday(Field):
    value: date
    def __init__(self, value: str):
        # try parse str to datetime obj by format "%d.%m.%Y").date() or except ValueError:
        #     raise ValueError("Invalid date format. Use DD.MM.YYYY")
        pass

    def __str__(self):
        # return value turn to str with format "%d.%m.%Y"
        pass

@dataclass
class Email(Field):
    value: str
    def __init__(self, value: str):
        # raise ValueError("Invalid email format. Use 'user.name@example.com'") if validation return false or value = value.strip()
        pass

@dataclass
class Note(Field):
    value: str
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str):
       pass

    def search_tag(self, keyword: str) -> bool:
        pass

