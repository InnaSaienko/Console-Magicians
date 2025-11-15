import json
from pathlib import Path
from handlers.decorator_error import input_error

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)

@input_error
def handle_add_contact():
    pass

def update_phone():
    pass # return True if phone was updated else False

@input_error
def handle_update_phone():
    # msg = MESSAGES["change_success"] if update_phone() else MESSAGES["contact_not_found"]
    # return msg
    pass

@input_error
def handle_delete_contact():
    pass

@input_error
def handle_show_phone():
    pass # book.find(name.title())

@input_error
def handle_show_email():
    pass

@input_error
def handle_show_address():
    pass

@input_error
def handle_show_all_contacts():
    pass

@input_error
def handle_upcoming_birthdays():
    pass

def handle_welcome(_args, _book):
    return MESSAGES["welcome"]


def handle_exit(_args, _book):
    raise StopIteration()