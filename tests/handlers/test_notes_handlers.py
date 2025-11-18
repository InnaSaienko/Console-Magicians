from unittest import TestCase
from unittest.mock import Mock

from book.fields_type import Note
from handlers.notes_handlers import handle_add_note

class NotesHandlersTest(TestCase):
    """Covers notes handlers with tests"""

    def test_add_note_pass(self):
        """Verify happy path flow"""
        args = ("name", "note", "tag")
        book = Mock()
        record = Mock()
        book.find.return_value = record

        msg = handle_add_note(args, book)

        self.assertEqual(msg, "Note was successfully added")
        book.find.assert_called_once_with(args[0])
        note = Note(args[1])
        note.add_tag(args[2])
        record.add_note.assert_called_once_with(note)

    def test_add_note_fail(self):
        """Verify corresponding messages is returned when name is not found"""
        args = ("name", "note", "tag")
        book = Mock()
        book.find.return_value = None

        msg = handle_add_note(args, book)

        self.assertEqual(msg, "Contact not found.")
