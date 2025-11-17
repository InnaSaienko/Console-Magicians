"""Contact record class with all related fields and methods."""
from dataclasses import dataclass, field
from typing import List, Optional

from book.fields_type import Address, Birthday, Email, Name, Note, Phone


@dataclass
class Record:
    """Contact record containing name, phones, emails, birthday, etc."""

    name: Name
    birthday: Optional[Birthday] = None
    phones: List[Phone] = field(default_factory=list)
    emails: List[Email] = field(default_factory=list)
    address: Optional[Address] = None
    notes: List[Note] = field(default_factory=list)

    def __str__(self):
        phone_str = "; ".join(p.value for p in self.phones)
        return (
            f"Contact name: {self.name.value}, "
            f"birthday: {self.birthday}, phones: {phone_str}"
        )

    def add_phone(self, phone: str) -> bool:
        self.phones.append(Phone(phone))
        return True

    def add_email(self, email: str) -> bool:
        self.emails.append(Email(email))
        return True

    def add_birthday(self, birthday) -> bool:
        self.birthday = Birthday(birthday)
        return True

    def add_address(self, address_str: str) -> bool:
        self.address = Address(address_str)
        return True

    def find_phone(self, phone: str) -> Optional[Phone]:
        return next((p for p in self.phones if p.value == phone), None)

    def remove_phone(self, phone: str) -> bool:
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            return True
        return False

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone
            return True
        return False

    def add_note(self, note_obj: Note) -> bool:
        self.notes.append(note_obj)
        return True

    def find_note_by_text(self, text: str) -> Optional[Note]:
        return next((n for n in self.notes if text in n.value.lower()), None)

    def delete_note(self, text_keyword: str) -> bool:
        note_to_delete = self.find_note_by_text(text_keyword)
        if note_to_delete:
            self.notes.remove(note_to_delete)
            return True
        return False

    def update_note(self, old_text_keyword: str, new_text: str) -> bool:
        note = self.find_note_by_text(old_text_keyword)
        if note:
            note.value = new_text
            return True
        return False

    def find_notes_by_tag(self, tag: str) -> list[Note]:
        normalized = tag.strip().lower()
        return [
            note
            for note in self.notes
            if normalized in (t.lower() for t in note.tags)
        ]

    def add_tag(self, note_text_keyword: str, tag: str) -> bool:
        note = self.find_note_by_text(note_text_keyword)
        if note:
            return note.add_tag(tag.lower())
        return False

    def change_tag(
            self,
            note_text_keyword: str,
            old_tag: str,
            new_tag: str
    ) -> bool:
        note = self.find_note_by_text(note_text_keyword)
        return note.update_tag(old_tag, new_tag)

    def delete_tag(self, note_keyword: str, tag_to_delete: str) -> bool:
        note = self.find_note_by_text(note_keyword)
        if note:
            return note.delete_tag(tag_to_delete)
        return False

    def find_email(self, email: str) -> Email | None:
        for email_obj in self.emails:
            if email_obj.value == email:
                return email_obj
        return None

    def update_email(self, old_email: str, new_email: str) -> bool:
        for email_obj in self.emails:
            if email_obj.value == old_email:
                email_obj.value = new_email
                return True
        return False

    def update_birthday(self, value: Birthday):
        self.birthday = value
