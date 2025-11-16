import json
from pathlib import Path

from book.record import Record
from book.fields_type import Name, Birthday
from display.display_records import show_records
from utils.validation_birthday import validation_birthday
from utils.validation_email import validation_email
from utils.validation_phone import validation_phone
from decorators.decorator_error import input_error
from rich.table import Table
from rich.console import Console

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)

@input_error
def handle_add_contact(args, book):
    name, phone,*rest = args
    email = rest[0] if rest else None
    record = book.find(name.lower())
    if record is None:
        record = Record(Name(name))
        record.add_phone(phone)
        book.add_record(record)
        if email:
            record.add_email(email)
        return MESSAGES["contact_added"]
    else:
        record.add_phone(phone)
    return MESSAGES["change_success"]

@input_error
def handle_update_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    old_phone = validation_phone(old_phone)
    new_phone = validation_phone(new_phone)
    is_edited = record.edit_phone(old_phone, new_phone)
    return MESSAGES["phone_updated"] if is_edited else MESSAGES ['phone_not_found']

@input_error
def handle_delete_contact(args, book):
    name, *rest = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES ['contact_not_found']
    is_deleted = book.delete(record.name.value)
    return MESSAGES["success_deleted"] if is_deleted else MESSAGES ['contact_not_found']

@input_error
def handle_show_phone(args, book):
    name, *rest = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES["contact_not_found"]
    if not found_record.phones:
        return MESSAGES["phones_no_data"]
    return f'Phones: {'; '.join(item.value for item in found_record.phones)}'

@input_error
def handle_add_email(args, book):
    name, email = args
    record = book.find(name.lower())
    if record is None:
        record = Record(Name(name))
        book.add_record(record)
        is_new = True
    record.add_email(email)
    return MESSAGES["contact_added"]

@input_error
def handle_show_email(args, book):
    name, *rest = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES["contact_not_found"]
    if not found_record.emails:
        return MESSAGES["emails_no_data"]
    return f'Emails: {'; '.join(item.value for item in found_record.emails)}'

def handle_show_address(args, book):
    name, *rest = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES["contact_not_found"]
    if found_record.address is None:
        return MESSAGES["address-not-found"]
    return f"Address for {found_record.name.value}: {found_record.address.value}"

@input_error
def handle_show_all_contacts(args, book):
    if book.is_empty():
        return MESSAGES["empty_book"]

    show_records(book.get_all_records())
    return None


@input_error
def handle_show_birthday(args, book):
    name, *rest = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    if not record:
        return MESSAGES["contact_not_found"]
    if not record.birthday:
        return MESSAGES["birthday_not_found"]
    return f"Birthday: {record.birthday}"

@input_error
def handle_find_contact(args, book):
    name, *rest = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    return str(record)

@input_error
def handle_upcoming_birthdays(args, book):
    if book.is_empty():
        return MESSAGES["empty_book"]
    upcoming_list = book.get_upcoming_birthdays()
    if not upcoming_list:
        return "No upcoming birthdays found"
    
    table = Table(title="Upcoming Birthdays")
    table.add_column("Contact Name", style="cyan", no_wrap=True)
    table.add_column("Congratulation Date", style="magenta")

    for item in upcoming_list:
        table.add_row(item['name'], item['date'])
    console = Console()
    console.print(table)    
        
    return ""


@input_error
def handle_add_birthday(args, book):
    name, birthday = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    record.add_birthday(birthday)
    return MESSAGES["birthday_added"]

def handle_welcome(_args, _book):
    return MESSAGES["welcome"]


def handle_exit(_args, _book):
    raise StopIteration()


@input_error
def handle_update_email(args, book):
    name, old_email, new_email = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    email = record.find_email(old_email)
    if not email:
        return MESSAGES["email_not_found"]
    if not validation_email(new_email):
        return MESSAGES["email_validation_error"]
    if not validation_email(old_email):
        return MESSAGES["email_validation_error"]
    record.update_email(old_email, new_email)
    return MESSAGES['email_updated']

@input_error
def handle_update_birthday(args, book):
    name, birthday = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    if not validation_birthday(birthday):
        return MESSAGES['birthday_validation_error']
    record.update_birthday(Birthday(birthday))
    return MESSAGES['birthday_updated']

@input_error
def handle_find_email(args, book):
    email, *rest = args
    records = book.find_by_email(email)
    if not records:
        return MESSAGES["contact_not_found"]

    return show_records(records)

@input_error
def handle_find_birthday(args, book):
    birthday, *rest = args
    records = book.find_by_birthday(birthday)
    if not records:
        return MESSAGES["contact_not_found"]

    return show_records(records)


@input_error
def handle_add_address(args, book):
    name = args[0]
    address_parts = args[1:] 
    address_str = " ".join(address_parts)
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]
    record.add_address(address_str)
    return MESSAGES["address_added"]