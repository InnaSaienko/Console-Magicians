import json
from pathlib import Path

from book.book import Book
from book.fields_type import Note
from decorators.decorator_args import validate_args
from decorators.decorator_error import input_error
from display.display_notes import show_notes_for_record

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)


@input_error
@validate_args(
    required=2,
    optional=1,
    error_msg='Expected command format: add-note NAME "NOTE TEXT" ["TAG..."]',
)
def handle_add_note(args, book: Book):
    name, note_text, *tags_text = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    note = Note(note_text)
    if tags_text:
        tags = tags_text[0].lower().split()
        for tag in tags:
            note.add_tag(tag)

    record.add_note(note)
    return MESSAGES["note_added"]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg='Expected command format: add-tag NAME "KEYWORDS" NEW TAG',
)
def handle_add_tag(args, book: Book):
    name, keywords, new_tag = args
    new_tag = new_tag.lower()
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    matched_notes = []
    for kw in keywords.split():
        matched_notes = [
            n for n in record.notes if kw in n.value
        ]
        if matched_notes:
            break
    for note in matched_notes:
        if new_tag not in note.tags:
            note.add_tag(new_tag)
        return MESSAGES["add_tag"]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg='Expected command format: update-note NAME KEYWORD "NOTE TEXT"',
)
def handle_update_note(args, book: Book):
    name, keyword, new_note = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    updated = record.update_note(keyword, new_note.lower())
    return (
        MESSAGES["note_updated"]
        if updated
        else MESSAGES["note_does_not_exist"]
    )



@input_error
@validate_args(
    required=4,
    optional=0,
    error_msg="Expected command format: change-tag NAME KEYWORD OLDTAG NEWTAG",
)
def handle_change_tag(args, book: Book):
    name, keyword, old_tag, new_tag = args
    record = book.find(name.lower())

    if not record:
        return MESSAGES["contact_not_found"]

    updated = record.change_tag(keyword.lower(), old_tag.lower(), new_tag.lower())
    return MESSAGES["tag_updated"] if updated else MESSAGES["no_find_tag"]



@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: delete-note NAME KEYWORD",
)
def handle_delete_note(args, book: Book):
    name, keyword = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    response = record.delete_note(keyword.lower())
    if response:
        return MESSAGES["note_deleted"]
    return MESSAGES["no_delete_note"]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg="Expected command format: delete-tag NAME NOTEKEYWORD TAG",
)
def handle_delete_tag(args, book: Book):
    name, note_keyword, tag_to_delete = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    response = record.delete_tag(note_keyword.lower(), tag_to_delete.lower())
    if response:
        return MESSAGES["tag_deleted"]
    return MESSAGES["no_find_tag"]


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-contact-notes NAMEG",
)
def handle_show_contact_notes(args, book: Book):
    (name,) = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    if not record.notes:
        return MESSAGES["note_does_not_exict"]

    show_notes_for_record(record)


@input_error
@validate_args(
    required=2,
    optional=0,
    error_msg="Expected command format: find-notes-by-tag NAME TAG"
)
def handle_find_notes_by_tag(args, book: Book) -> str | None:
    name, tag = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES["contact_not_found"]

    matches = record.find_notes_by_tag(tag.lower())
    if not matches:
        return MESSAGES["no_find_tag"]
    show_notes_for_record(matches)
