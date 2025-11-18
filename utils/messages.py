import json
from json import JSONDecodeError
from pathlib import Path

WELCOME_MESSAGE_KEY: str = "welcome"
GOODBYE_MESSAGE_KEY: str = "goodbye"

CONTACT_ADDED_MESSAGE_KEY: str = "contact_added"
CHANGE_SUCCESS_MESSAGE_KEY: str = "change_success"
CONTACT_NOT_FOUND_MESSAGE_KEY: str = "contact_not_found"
CONTACT_LIST_EMPTY_MESSAGE_KEY: str = "contact_list_empty"
SUCCESS_DELETED_MESSAGE_KEY: str = "success_deleted"
PHONE_NOT_FOUND_MESSAGE_KEY: str = "phone_not_found"
PHONES_NO_DATA_MESSAGE_KEY: str = "phones_no_data"
PHONE_UPDATED_MESSAGE_KEY: str = "phone_updated"

ADDRESS_EMPTY_MESSAGE_KEY: str = "address_empty"
ADDRESS_ADDED_MESSAGE_KEY: str = "address_added"
ADDRESS_NOT_FOUND_MESSAGE_KEY: str = "address-not-found"

BIRTHDAY_ADDED_MESSAGE_KEY: str = "birthday_added"
BIRTHDAY_UPDATED_MESSAGE_KEY: str = "birthday_updated"
BIRTHDAY_CONTACT_MISSING_MESSAGE_KEY: str = "birthday_contact_missing"
BIRTHDAY_NOT_FOUND_MESSAGE_KEY: str = "birthday_not_found"
BIRTHDAY_SHOW_FAIL_MESSAGE_KEY: str = "birthday_show_fail"
BIRTHDAY_VALIDATION_ERROR_MESSAGE_KEY: str = "birthday_validation_error"

INVALID_NAME_MESSAGE_KEY: str = "invalid_name"
INVALID_ARGS_MESSAGE_KEY: str = "invalid_args"
INVALID_VALUE_MESSAGE_KEY: str = "invalid_value"

UNKNOWN_COMMAND_MESSAGE_KEY: str = "unknown_command"
ERROR_OCCURRED_MESSAGE_KEY: str = "error_occurred"

NOTE_ADDED_MESSAGE_KEY: str = "note_added"
NOTE_UPDATED_MESSAGE_KEY: str = "note_updated"
NOTE_DOES_NOT_EXIST_MESSAGE_KEY: str = "note_does_not_exist"
NO_NOTES_EXIST_MESSAGE_KEY: str = "no_notes_exist"
NOTE_DELETED_MESSAGE_KEY: str = "note_deleted"

SHOW_ALL_TITLE_MESSAGE_KEY: str = "show_all_title"
SHOW_PHONE_TITLE_MESSAGE_KEY: str = "show_phone_title"

INPUT_PROMPT_MESSAGE_KEY: str = "input_prompt"
EMPTY_BOOK_MESSAGE_KEY: str = "empty_book"

TAG_UPDATED_MESSAGE_KEY: str = "tag_updated"
TAG_DELETED_MESSAGE_KEY: str = "tag_deleted"
NO_FIND_TAG_MESSAGE_KEY: str = "no_find_tag"

ADD_TAG_MESSAGE_KEY: str = "add_tag"

EMAIL_NO_DATA_MESSAGE_KEY: str = "email_no_data"
EMAIL_NOT_FOUND_MESSAGE_KEY: str = "email_not_found"
EMAIL_UPDATED_MESSAGE_KEY: str = "email_updated"
EMAIL_VALIDATION_ERROR_MESSAGE_KEY: str = "email_validation_error"
EMAIL_NO_DATA_MESSAGE_KEY: str = "email_no_data"


def _get_messages():
    message_file = Path("resources") / "messages.json"

    try:
        with open(message_file, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, JSONDecodeError, UnicodeDecodeError) as e:
        raise RuntimeError(f'Fatal: could not obtain interface massages from "{message_file}"') from e

def _validated_keys(messages: dict[str,str]) -> dict[str,str]:
    required_keys = set(v for k, v in globals().items() if k.endswith("_MESSAGE_KEY"))
    actual_keys = set(messages.keys())
    if missing_keys := required_keys - actual_keys:
        raise KeyError(
            "Error loading messages.json: key(s) "
            f"'{', '.join(missing_keys)}' were not found in messages.json"
        )
    return messages


MESSAGES = _validated_keys(_get_messages())
