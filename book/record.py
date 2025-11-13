from dataclasses import dataclass, field
from typing import List, Optional
from fields_type import Name, Phone, Birthday, Email, Note, Address


@dataclass
class Record:
    name: Name
    birthday: Optional[Birthday] = None
    phones: List[Phone] = field(default_factory=list)
    emails: List[Email] = field(default_factory=list)
    notes: List[Note] = field(default_factory=list)

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)
        email_str = '; '.join(e.value for e in self.emails) if self.emails else "N/A"
        address_str = f", Address: {self.address.value}" if self.address else ""
        birthday_str = f", Birthday: {self.birthday}" if self.birthday else ""
        return (
            f"Contact name: {self.name.value}"
            f"{birthday_str}" 
            f"{address_str}"
            f", Email: {email_str}"
            f", Phone: {phone_str}"
        )

    def add_phone(self, phone: str) -> bool:
        try:
            self.phones.append(Phone(phone))
            return True
        except ValueError:
            return False

    def add_email(self, email: str) -> bool:
        try:
            self.emails.append(Email(email))
            return True
        except ValueError:
            return False

    def add_birthday(self, birthday) -> bool:
        try:
            self.birthday = Birthday(birthday)
            return True
        except ValueError:
            return False
        
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
        phone = self.find_phone(old_phone)
        if phone:
            try:
                validated_new_phone = Phone(new_phone) 
                index = self.phones.index(phone)
                self.phones[index] = validated_new_phone
                return True
            except ValueError:
                return False
        return False   
