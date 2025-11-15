from collections import UserDict
from typing import Optional
from book.record import Record
from utils.get_upcoming_birthdays import get_birthdays


class Book(UserDict):
    def add_record(self, record: Record) -> bool:
        self.data[record.name.value] = record
        return True

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True        
        else:
            return False

    def find_by_email(self, email: str) -> list[Record] | None:
        result = []
        for record in self.data.values():
            if record.find_email(email):
                result.append(record)
        return result

    def find_by_birthday(self, birthday: str) -> list[Record] | None:
        result = []
        for record in self.data:
            if record.birthday == birthday:
                result.append(record)
        return result

    def is_empty(self) -> bool:
        return not self.data

    def get_upcoming_birthdays(self) -> list[dict]:
        return get_birthdays(self.data)