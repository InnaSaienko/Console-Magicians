from book.book import Book
from book.fields_type import Note
from decorators.decorator_args import validate_args
from decorators.decorator_error import input_error
from display.display_notes import show_notes_for_record
from utils.messages import (
    MESSAGES, CONTACT_NOT_FOUND_MESSAGE_KEY, NOTE_ADDED_MESSAGE_KEY,
    NO_FIND_TAG_MESSAGE_KEY, ADD_TAG_MESSAGE_KEY, NOTE_UPDATED_MESSAGE_KEY,
    TAG_UPDATED_MESSAGE_KEY, NOTE_DELETED_MESSAGE_KEY,
    TAG_DELETED_MESSAGE_KEY, NO_NOTES_EXIST_MESSAGE_KEY, NOTE_DOES_NOT_EXIST_MESSAGE_KEY
)

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
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    note = Note(note_text)
    if tags_text:
        tags = tags_text[0].lower().split()
        for tag in tags:
            note.add_tag(tag)

    record.add_note(note)
    return MESSAGES[NOTE_ADDED_MESSAGE_KEY]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg='Expected command format: add-tag NAME "KEYWORDS" NEW TAG',
)
def handle_add_tag(args, book: Book):
    name, keywords, new_tag = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    record.add_tag(keywords.lower().split(), new_tag.lower())
    return MESSAGES[ADD_TAG_MESSAGE_KEY]


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
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    updated = record.update_note(keyword.lower(), new_note.lower())
    return (
        MESSAGES[NOTE_UPDATED_MESSAGE_KEY]
        if updated
        else MESSAGES[NOTE_DOES_NOT_EXIST_MESSAGE_KEY]
    )


@input_error
@validate_args(
    required=4,
    optional=0,
    error_msg="Expected command format: change-tag NAME KEYWORD OLD_TAG NEW_TAG"
)
def handle_change_tag(args, book: Book):
    name, keyword, old_tag, new_tag = args
    record = book.find(name.lower())

    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    updated = record.change_tag(keyword.lower(), old_tag.lower(), new_tag.lower())
    return MESSAGES[TAG_UPDATED_MESSAGE_KEY] if updated else MESSAGES[NO_FIND_TAG_MESSAGE_KEY]



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
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    response = record.delete_note(keyword.lower())
    if response:
        return MESSAGES[NOTE_DELETED_MESSAGE_KEY]
    return MESSAGES[NOTE_DOES_NOT_EXIST_MESSAGE_KEY]


@input_error
@validate_args(
    required=3,
    optional=0,
    error_msg="Expected command format: delete-tag NAME KEYWORD TAG"
)
def handle_delete_tag(args, book: Book):
    name, note_keyword, tag_to_delete = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    response = record.delete_tag(note_keyword.lower(), tag_to_delete.lower())
    if response:
        return MESSAGES[TAG_DELETED_MESSAGE_KEY]
    return MESSAGES[NO_FIND_TAG_MESSAGE_KEY]


@input_error
@validate_args(
    required=1,
    optional=0,
    error_msg="Expected command format: show-contact-notes NAME"
)
def handle_show_contact_notes(args, book: Book):
    (name,) = args
    record = book.find(name.lower())
    if not record:
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    if not record.notes:
        return MESSAGES[NO_NOTES_EXIST_MESSAGE_KEY]

    show_notes_for_record(record)
    return ""


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
        return MESSAGES[CONTACT_NOT_FOUND_MESSAGE_KEY]

    matches = record.find_notes_by_tag(tag.lower())
    if not matches:
        return MESSAGES[NO_FIND_TAG_MESSAGE_KEY]

    show_notes_for_record(matches)
    return ""