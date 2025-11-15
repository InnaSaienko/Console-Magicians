from handlers.book_handlers import (handle_add_contact,
                                    handle_update_phone,
                                    handle_delete_contact,
                                    handle_show_phone, handle_show_all_contacts, handle_upcoming_birthdays,
                                    handle_add_birthday, handle_show_birthday, handle_find_contact, handle_update_email,
                                    handle_update_birthday, handle_find_email, handle_find_birthday, handle_add_address,handle_show_email,handle_add_email,handle_show_address)
from handlers.common_handlers import handle_exit, handle_hello
from handlers.notes_handlers import handle_add_note, handle_delete_note, handle_update_note, handle_add_tag, \
    handle_update_tag, handle_show_contact_notes, handle_find_notes_by_tag, handle_delete_tag

COMMAND_TO_HANDLER = {
    'add-contact': handle_add_contact,
    'add-birthday': handle_add_birthday,
    'add-email':handle_add_email,
    'update-phone': handle_update_phone,
    'update-email': handle_update_email,
    'update-birthday': handle_update_birthday,
    'show-birthday': handle_show_birthday,
    'show-email':handle_show_email,
    'show-address':handle_show_address,
    'upcoming-birthdays': handle_upcoming_birthdays,
    'add-address': handle_add_address,
    'find-contact': handle_find_contact,
    'find-email': handle_find_email,
    'find-birthday': handle_find_birthday,
    'delete-contact': handle_delete_contact,
    'show-phone': handle_show_phone,
    'all-contact': handle_show_all_contacts,

    "add-note": handle_add_note,
    "delete-note": handle_delete_note,
    "update-note": handle_update_note,
    "show-contact-notes": handle_show_contact_notes,
    "find-notes-by-tag": handle_find_notes_by_tag,

    "add-tag": handle_add_tag,
    "change-tag": handle_update_tag,
    "delete-contact-tag": handle_delete_tag,

    "hello": handle_hello,
    "close": handle_exit,
    "exit": handle_exit,
}