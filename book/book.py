from collections import UserDict
from typing import Optional
from records import Record

from utils.get_upcoming_birthdays import get_birthdays


class Book(UserDict):
    def add_record(self, record: Record) -> bool:
        # some code
        return True

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if True:
            return True
        else:
            return False


    def get_upcoming_birthdays(self) -> list[dict]:
        # get_birthdays(self.data)
        pass