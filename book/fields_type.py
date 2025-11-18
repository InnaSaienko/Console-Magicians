"""Field types for contact records."""
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List

from utils.validation_email import validation_email
from utils.validation_phone import validation_phone


@dataclass
class Field:
    """Base class for all field types."""

    value: str

    def __str__(self) -> str:
        return self.value


@dataclass
class Name(Field):
    """Name field with automatic normalization."""

    value: str

    def __init__(self, value: str):
        self.value = value.strip().lower()


@dataclass
class Phone(Field):
    """Phone field with validation."""

    value: str

    def __post_init__(self):
        self.value = validation_phone(self.value)


@dataclass
class Birthday(Field):
    """Birthday field with date validation."""

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
    """Email field with validation."""

    value: str

    def __init__(self, value: str):
        if not validation_email(value):
            raise ValueError(
                "Invalid email format. Use 'user.name@example.com'"
            )
        self.value = value.strip()


@dataclass
class Note(Field):
    """Note field with tags support."""

    value: str
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> bool:
        """Add one or more space-separated tags."""
        parts = [t.strip().lower() for t in tag.split() if t.strip()]
        added = False
        for p in parts:
            if p not in self.tags:
                self.tags.append(p)
                added = True
        return added

    def search_tag(self, keyword: str):
        """Search for a tag by keyword."""
        if not keyword:
            raise ValueError("Invalid tag format.")

        if keyword.lower() in self.tags:
            return keyword.lower()
        return False

    def delete_tag(self, tag: str) -> bool:
        """Delete a tag from the note."""
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False


@dataclass
class Address(Field):
    """Address field."""

    value: str

    def __init__(self, value: str):
        self.value = value.strip()
