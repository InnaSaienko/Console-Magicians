from dataclasses import dataclass, field
from typing import List, Optional
from fields_type import Name, Phone, Birthday, Email, Note


@dataclass
class Record:
    name: Name
    birthday: Optional[Birthday] = None
    phones: List[Phone] = field(default_factory=list)
    emails: List[Email] = field(default_factory=list)
    notes: List[Note] = field(default_factory=list)

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {phone_str}"

    def add_phone(self, phone: str) -> bool:
        pass

    def add_email(self, email: str) -> bool:
       pass

    def add_birthday(self, birthday) -> bool:
        # some code
        return True

    def add_note(self, note: Note) -> bool:
        # some code
        return True

    def find_notes_by_tag(self, tag: str) -> list[Note]:
        # use return comprehension for iterate through a list of notes for return all matched by tag notes
        pass


    def find_phone(self, phone: str) -> Optional[Phone]:
        # return phone for phone in phones if phone.value == phone
        # next(phone,  None)
        pass

    def remove_phone(self, phone: str) -> bool:
        # return True if self.find_phone(phone) else return False
        pass

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
       # return True if phone was updated else False
        pass

    def find_email(self, email: str) -> Email | None:
        for email in self.emails:
            if email.value == email:
                return email
        return None

    def update_email(self, old_email: str, new_email: str) -> bool:
        for email in self.emails:
            if email.value == old_email:
                email.value = new_email
                return True
        return False

    def update_birthday(self, value: Birthday):
        self.birthday = value


