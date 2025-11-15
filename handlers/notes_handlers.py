import json
from pathlib import Path

from book.book import Book
from book.fields_type import Note
from handlers.decorator_error import input_error
from display.display_notes import show_notes_for_record

BASE_DIR = Path(__file__).resolve().parent.parent
MESSAGES_PATH = BASE_DIR / "utils" / "messages.json"

with open(MESSAGES_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)


@input_error
def handle_add_note(args, book: Book):
    name, note, *tags = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    note_obj = Note(note)
    for tag in tags:
        note_obj.add_tag(tag)

    record.add_note(note_obj)
    return MESSAGES["note_added"]


@input_error
def handle_add_tag(args, book: Book):
    name, keywords, new_tag = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    matched_notes = []
    for kw in keywords:
        matched_notes = [n for n in record.notes if kw.lower() in n.value.lower()]
        if matched_notes:
            break
    for note in matched_notes:
        if new_tag not in note.tags:
            note.add_tag(new_tag)
        return MESSAGES["add_tag"]
    

@input_error
def handle_update_note(args, book: Book):
    name, keyword, new_note = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    updated = record.update_note(keyword, new_note)
    msg = MESSAGES["note_updated"] if updated else MESSAGES["note_does_not_exict"]
    return msg


@input_error
def handle_update_tag(args, book: Book):
    name, keyword, old_tag, new_tag = args
    record = book.find(name.title())

    if not record:
        return MESSAGES["contact_not_found"]
    updated = record.update_tag(keyword, old_tag, new_tag)
    msg = MESSAGES["tag_updated"] if updated else MESSAGES["no_find_tag"]
    return msg

@input_error
def handle_delete_note(args, book: Book):
    name, keyword = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    response = record.delete_note(keyword)
    if response:
        return MESSAGES["note_deleted"]
    return MESSAGES["no_delete_note"]


@input_error
def handle_delete_tag(args, book: Book):
    name, keyword, tag_to_delete = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    response = record.delete_note(keyword, tag_to_delete)
    if response:
        return MESSAGES["tag_deleted"]
    return MESSAGES["no_find_tag"]

@input_error
def handle_show_notes(args, book: Book):
    name, *rest = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    if not record.notes:
        return MESSAGES["note_does_not_exict"]

    show_notes_for_record(record)
    return ""


@input_error
def handle_find_notes_by_tag(args, book: Book) -> str | list[str]:
    name, tag = args
    record = book.find(name.title())
    if not record:
        return MESSAGES["contact_not_found"]

    matches = record.find_notes_by_tag(tag)
    if not matches:
        return MESSAGES["no_find_tag"]

    return "\n".join(
        f"{i + 1}. {n.value} [tags: {', '.join(n.tags)}]" for i, n in enumerate(matches)
    )
