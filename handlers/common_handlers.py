from display.display_help import show_help
from utils.messages import MESSAGES, WELCOME_MESSAGE_KEY

def handle_hello(_args, _book):
    return MESSAGES[WELCOME_MESSAGE_KEY]


def handle_help(_args, _book):
    return show_help()


def handle_exit(_args, _book):
    raise StopIteration()
