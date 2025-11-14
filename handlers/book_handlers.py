import json
from pathlib import Path
from book.record import Record
from book.fields_type import Name
from display.display_records import show_records
from utils.validation_phone import validation_phone
from handlers.decorator_error import input_error

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)

@input_error
def handle_add_contact(args, book):
    name, phone, email = args
    record = book.data.get(name)
    if record is None:
        record = Record(Name(name))
        record.add_phone(phone)
        record.add_email(email)
        book.add_record(record)
        return MESSAGES["contact_added"]
    else:
        record.add_phone(phone)
    return MESSAGES["change_success"]

@input_error
def handle_update_phone(args, book):
    name, old_phone, new_phone = args
    record = book.data.get(name)
    old_phone = validation_phone(old_phone)
    new_phone = validation_phone(new_phone)
    if record:
        for phone in record.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return True
            return False

    return False

@input_error
def handle_delete_contact(args, book):
    name, *rest = args
    is_deleted = book.delete(name)
    if is_deleted:
        return MESSAGES["success_deleted"]
    return MESSAGES["contact_not_found"]

@input_error
def handle_show_phone(args, book):
    name, *rest = args
    found_record = book.get(name)
    if found_record is None:
        return MESSAGES["contact_not_found"]
    count_phones = len(found_record.phones)
    if count_phones == 0:
        return MESSAGES["phones_no_data"]
    return f'Phones: {','.join(found_record.phones)}'

@input_error
def handle_show_email(args, book):
    name, *rest = args
    found_record = book.get(name)
    if found_record is None:
        return MESSAGES["contact_not_found"]
    count_phones = len(found_record.phones)
    if count_phones == 0:
        return MESSAGES["phones_no_data"]
    return f'Phones: {','.join(found_record.phones)}'

def handle_show_address(args, book):
    pass # Neither book nor record has an address field.

@input_error
def handle_show_all_contacts(args, book):
    if book.is_empty():
        return MESSAGES["empty_book"]

    show_records(book.data)
    return None


@input_error
def handle_upcoming_birthdays(args, book):
    if book.is_empty():
        return MESSAGES["empty_book"]
    for item in book.get_upcoming_birthdays():
        print(f'User={item.name}, birthday={item.congratulation_date}')
    return None

def handle_welcome(_args, _book):
    return MESSAGES["welcome"]


def handle_exit(_args, _book):
    raise StopIteration()