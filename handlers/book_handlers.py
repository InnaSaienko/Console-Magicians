import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)


def handle_add_contact():
    pass

def update_phone():
    pass # return True if phone was updated else False

def handle_update_phone():
    # msg = MESSAGES["change_success"] if update_phone() else MESSAGES["contact_not_found"]
    # return msg
    pass

def handle_delete_contact():
    pass

def handle_show_phone():
    pass # book.find(name.title())

def handle_show_email():
    pass

def handle_show_address():
    pass

def handle_show_all_contacts():
    pass

def handle_upcoming_birthdays():
    pass


def handle_welcome(_args, _book):
    return MESSAGES["welcome"]


def handle_exit(_args, _book):
    raise StopIteration()