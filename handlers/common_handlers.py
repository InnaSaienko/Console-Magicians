from display.display_help import show_help
from handlers.book_handlers import MESSAGES


def handle_hello(_args, _book):
    return MESSAGES["welcome"]


def handle_help(_args, _book):
    return show_help()


def handle_exit(_args, _book):
    raise StopIteration()
