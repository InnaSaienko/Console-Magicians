from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List

from utils.validation_email import validation_email
from utils.validation_phone import validation_phone


@dataclass
class Field:
    value: str
    def __str__(self) -> str:
        return self.value


@dataclass
class Name(Field):
    value: str
    def __init__(self, value: str):
        self.value = value.strip().lower()

@dataclass
class Phone(Field):
    value: str

    def __post_init__(self):
        self.value = validation_phone(self.value)

@dataclass
class Birthday(Field):
    value: date
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

@dataclass
class Email(Field):
    value: str
    def __init__(self, value: str):
        if not validation_email(value):
            raise ValueError("Invalid email format. Use 'user.name@example.com'")
        self.value = value.strip()

@dataclass
class Note(Field):
    value: str
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> bool:
        if tag and tag.strip() not in self.tags:
            self.tags.append(tag.strip())
            return True
        return False

    def search_tag(self, keyword: str):
        if not keyword:
            raise ValueError("Invalid tag format.")
        
        if keyword.lower() in self.tags:
            return keyword.lower()
        return False

    def delete_tag(self, tag: str) -> bool:
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

