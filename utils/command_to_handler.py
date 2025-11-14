from handlers.book_handlers import (handle_add_contact,
                                    handle_update_phone,
                                    handle_delete_contact,
                                    handle_show_phone)

COMMAND_TO_HANDLER = {
    "add-contact": handle_add_contact,
    "update-contact": handle_update_phone,
    "delete-contact": handle_delete_contact,
    "show-phone": handle_show_phone
}