from book.fields_type import Birthday, Name
from book.record import Record
from decorators.decorator_args import validate_args
from decorators.decorator_error import input_error
from display.display_records import show_records
from display.display_upcoming_birthdays import show_birthdays
from utils.validation_birthday import validation_birthday
from utils.validation_email import validation_email
from utils.validation_phone import validation_phone

from utils.messages import (
    MESSAGES, CONTACT_ADDED_MESSAGE_KEY, CHANGE_SUCCESS_MESSAGE_KEY,
    CONTACT_NOT_FOUND_MESSAGE_KEY, ADDRESS_ADDED_MESSAGE_KEY,
    PHONE_UPDATED_MESSAGE_KEY, PHONE_NOT_FOUND_MESSAGE_KEY,
    SUCCESS_DELETED_MESSAGE_KEY, PHONES_NO_DATA_MESSAGE_KEY,
    EMAIL_NO_DATA_MESSAGE_KEY, ADDRESS_NOT_FOUND_MESSAGE_KEY,
    EMPTY_BOOK_MESSAGE_KEY, BIRTHDAY_ADDED_MESSAGE_KEY,
    BIRTHDAY_NOT_FOUND_MESSAGE_KEY, EMAIL_NOT_FOUND_MESSAGE_KEY,
    EMAIL_UPDATED_MESSAGE_KEY, EMAIL_VALIDATION_ERROR_MESSAGE_KEY,
    BIRTHDAY_VALIDATION_ERROR_MESSAGE_KEY, BIRTHDAY_UPDATED_MESSAGE_KEY
)


@input_error
@validate_args(
    required=2,
    optional=1,
    error_msg="Expected command format: add-contact NAME PHONE [EMAIL]",
)
def handle_add_contact(args, book):
    name, phone, *rest = args
    email = rest[0] if rest else None
    record = book.find(name.lower())
    if record is None:
        record = Record(Name(name))
        record.add_phone(phone)
        if email:
            record.add_email(email)
        book.add_record(record)
        return MESSAGES[CONTACT_ADDED_MESSAGE_KEY]
    else:
        existing_phones = [p.value for p in record.phones]
        if phone in existing_phones:
            return f"The number {phone} already exists in the contact {name}."
        record.add_phone(phone)
    return MESSAGES[CHANGE_SUCCESS_MESSAGE_KEY]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg="Expected command format: update-phone NAME OLD-PHONE NEW-PHONE",
)
def handle_update_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    old_phone = validation_phone(old_phone)
    new_phone = validation_phone(new_phone)
    is_edited = record.edit_phone(old_phone, new_phone)
    return (
        MESSAGES[PHONE_UPDATED_MESSAGE_KEY] if is_edited else MESSAGES [PHONE_NOT_FOUND_MESSAGE_KEY]
    )

@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: delete-contact NAME",
)
def handle_delete_contact(args, book):
    (name,) = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES [CONTACT_NOT_FOUND_MESSAGE_KEY]
    is_deleted = book.delete(record.name.value)
    return (
        MESSAGES[SUCCESS_DELETED_MESSAGE_KEY]
        if is_deleted
        else MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    )

@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-phone NAME",
)
def handle_show_phone(args, book):
    (name,) = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    if not found_record.phones:
        return MESSAGES[PHONES_NO_DATA_MESSAGE_KEY]
    phones = "; ".join(item.value for item in found_record.phones)
    return f"Phones: {phones}"


@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: add-email NAME EMAIL",
)
def handle_add_email(args, book):
    name, email = args
    record = book.find(name.lower())
    if record is None:
        record = Record(Name(name))
        book.add_record(record)
    record.add_email(email)
    return MESSAGES[CONTACT_ADDED_MESSAGE_KEY]


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-email NAME",
)
def handle_show_email(args, book):
    (name,) = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    if not found_record.emails:
        return MESSAGES[EMAIL_NO_DATA_MESSAGE_KEY]
    emails = "; ".join(item.value for item in found_record.emails)
    return f"Emails: {emails}"


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-address NAME",
)
def handle_show_address(args, book):
    (name,) = args
    found_record = book.find(name.lower())
    if found_record is None:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    if found_record.address is None:
        return MESSAGES[ADDRESS_NOT_FOUND_MESSAGE_KEY]
    return (
        f"Address for {found_record.name.value}: {found_record.address.value}"
    )

@input_error
def handle_show_all_contacts(args, book):
    if book.is_empty():
        return MESSAGES[EMPTY_BOOK_MESSAGE_KEY]

    show_records(book.get_all_records())
    return None


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-birthday NAME",
)
def handle_show_birthday(args, book):
    (name,) = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    if not record.birthday:
        return MESSAGES[BIRTHDAY_NOT_FOUND_MESSAGE_KEY]
    return f"Birthday: {record.birthday}"


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: find-contact NAME",
)
def handle_find_contact(args, book):
    (name,) = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    return str(record)


@input_error
def handle_upcoming_birthdays(args, book):
    if book.is_empty():
        return MESSAGES[EMPTY_BOOK_MESSAGE_KEY]
    if args:
        days = int(args[0])
        upcoming_list = book.get_upcoming_birthdays(days)
    else:
        upcoming_list = book.get_upcoming_birthdays()
    show_birthdays(upcoming_list)
    return ""


@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: add-birthday NAME BIRTHDAY",
)
def handle_add_birthday(args, book):
    name, birthday = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    record.add_birthday(birthday)
    return MESSAGES[BIRTHDAY_ADDED_MESSAGE_KEY]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg="Expected command format: update-email NAME OLD_EMAIL NEW_EMAIL",
)
def handle_update_email(args, book):
    name, old_email, new_email = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    email = record.find_email(old_email)
    if not email:
        return MESSAGES[EMAIL_NOT_FOUND_MESSAGE_KEY]
    if not validation_email(new_email):
        return MESSAGES[EMAIL_VALIDATION_ERROR_MESSAGE_KEY]
    if not validation_email(old_email):
        return MESSAGES[EMAIL_VALIDATION_ERROR_MESSAGE_KEY]
    record.update_email(old_email, new_email)
    return MESSAGES[EMAIL_UPDATED_MESSAGE_KEY]


@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: update-birthday NAME BIRTHDAY",
)
def handle_update_birthday(args, book):
    name, birthday = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    if not validation_birthday(birthday):
        return MESSAGES[BIRTHDAY_VALIDATION_ERROR_MESSAGE_KEY]
    record.update_birthday(Birthday(birthday))
    return MESSAGES[BIRTHDAY_UPDATED_MESSAGE_KEY]


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: find-email EMAIL",
)
def handle_find_email(args, book):
    (email,) = args
    records = book.find_by_email(email)
    if not records:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    return show_records(records)


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: find-birthday BIRTHDAY",
)
def handle_find_birthday(args, book):
    (birthday,) = args
    records = book.find_by_birthday(birthday)
    if not records:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    return show_records(records)


@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: add-address NAME ADDRESS",
)
def handle_add_address(args, book):
    name, address = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]
    record.add_address(address)
    return MESSAGES[ADDRESS_ADDED_MESSAGE_KEY]
