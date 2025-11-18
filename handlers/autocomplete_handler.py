import shlex

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

from utils.command_to_handler import COMMAND_TO_HANDLER


class HintsCompleter(Completer):
    def __init__(self, hints):
        self.hints = hints

    def get_completions(self, document, complete_event):
        if document.text_before_cursor.endswith(" "):
            return
        word = document.get_word_before_cursor().lower()
        for hint in self.hints:
            if hint.startswith(word):
                yield Completion(hint, start_position=-len(word))


def parse_input(user_input):
    parts = shlex.split(user_input)
    cmd, *args = parts
    cmd = cmd.lower()
    return cmd, args


def read_input():
    session = PromptSession()
    commands = HintsCompleter(hints=COMMAND_TO_HANDLER.keys())

    try:
        user_input = session.prompt("Enter a command: ", completer=commands)
        command, args = parse_input(user_input)
    except (EOFError, KeyboardInterrupt):
        command, args = "exit", []

    return command, args
