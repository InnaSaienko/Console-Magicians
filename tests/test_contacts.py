from handlers.book_handlers import (
    handle_add_contact, handle_add_birthday, handle_update_birthday,
    handle_show_birthday, handle_find_birthday, handle_add_email,
    handle_update_email, handle_show_email, handle_find_email,
    handle_update_phone, handle_show_phone, handle_add_address,
    handle_show_address, handle_upcoming_birthdays, handle_find_contact,
    handle_delete_contact, handle_show_all_contacts 
)
from handlers.notes_handlers import (
    handle_add_note, handle_change_tag, handle_delete_tag, handle_add_tag, handle_update_note, handle_delete_note, 
    handle_find_notes_by_tag, handle_show_contact_notes
)


def test_add_contact(book):
    msg = handle_add_contact(["Hermione", "+48662767912", "h.granger@yahoo.com"], book)
    assert msg is not None
    assert book.find("hermione")


def test_update_phone(book):
    handle_add_contact(["Harry", "+380504556787", "potter@ukr.net"], book)
    msg = handle_update_phone(["Harry", "+380504556787", "+44-20-7123-4564"], book)
    assert msg is not None
    assert book.find("harry").phones[0].value == "+442071234564"


def test_show_phone(book):
    handle_add_contact(["Ron", "+380504556789"], book)
    result = handle_show_phone(["Ron"], book)
    assert "+380504556789" in result


def test_add_birthday(book):
    handle_add_contact(["Harry", "+81-50-3816-2787"], book)
    msg = handle_add_birthday(["Harry", "31.07.1980"], book)
    assert msg is not None
    assert "1980" in handle_show_birthday(["Harry"], book)


def test_update_birthday(book):
    handle_add_contact(["Ron", "+380504556789"], book)
    handle_add_birthday(["Ron", "01.03.1980"], book)
    msg = handle_update_birthday(["Ron", "24.11.1980"], book)
    assert msg is not None
    assert "24.11.1980" in handle_show_birthday(["Ron"], book)


def test_find_birthday(book):
    handle_add_contact(["Hermione", "+48662767912"], book)
    handle_add_birthday(["Hermione", "19.09.1979"], book)
    res = handle_find_birthday(["19.09.1979"], book)
    assert res is None  # show_records prints output but returns None


def test_add_email(book):
    handle_add_contact(["Ron", "+380504556789"], book)
    msg = handle_add_email(["Ron", "wizzzlly@gmail.com"], book)
    assert msg is not None
    assert " wizzzlly@gmail.com" in handle_show_email(["Ron"], book)


def test_update_email(book):
    handle_add_contact(["Hagrid", "+44-20-7123-4557", "h@old.com"], book)
    msg = handle_update_email(["Hagrid", "h@old.com", "h@new.com"], book)
    assert msg is not None
    assert "h@new.com" in handle_show_email(["Hagrid"], book)


def test_find_email(book):
    handle_add_contact(["Luna", "+48798663456", "luna@shine.com"], book)
    result = handle_find_email(["luna@shine.com"], book)
    assert result is None  # show_records prints output


def test_add_address(book):
    handle_add_contact(["Harry", "+81-50-3816-2787"], book)
    msg = handle_add_address(["Harry", "privet drive"], book)
    assert msg is not None
    assert "privet drive" in handle_show_address(["Harry"], book)


def test_show_address(book):
    handle_add_contact(["Ron", "+380504556789"], book)
    handle_add_address(["Ron", "burrow"], book)
    res = handle_show_address(["Ron"], book)
    assert "burrow" in res


def test_find_contact(book):
    handle_add_contact(["Neville", "+380504556778"], book)
    res = handle_find_contact(["Neville"], book)
    assert "Neville".lower() in res


def test_all_contacts(book):
    handle_add_contact(["Harry", "+81-50-3816-2787"], book)
    handle_add_contact(["Ron", "+380504556789"], book)
    assert handle_show_all_contacts([], book) is None


def test_delete_contact(book):
    handle_add_contact(["Draco", "+380504556722"], book)
    msg = handle_delete_contact(["Draco"], book)
    assert msg is not None
    assert book.find("draco") is None


def test_upcoming_birthdays(book):
    handle_add_contact(["Test", "+380504556744"], book)
    handle_add_birthday(["Test", "01.01.2000"], book)
    assert handle_upcoming_birthdays([], book) is None


def test_add_note(book):
    handle_add_contact(["Harry", "+380501112233"], book)

    msg = handle_add_note(["Harry", "My note text", "magic important"], book)
    assert "added" in msg.lower()

    record = book.find("harry")
    assert len(record.notes) == 1
    assert record.notes[0].value == "My note text"
    assert "magic" in record.notes[0].tags
    assert "important" in record.notes[0].tags


def test_add_tag(book):
    handle_add_contact(["ron", "+380988303034"], book)
    handle_add_note(["ron", "Buy wand", "shop"], book)

    msg = handle_add_tag(["ron", "buy", "magic"], book)
    assert "tag" in msg.lower()

    record = book.find("ron")
    assert "magic" in record.notes[0].tags
    

def test_update_note(book):
    handle_add_contact(["Luna", "+380981234567"], book)
    handle_add_note(["Luna", "Old note", "dream"], book)

    msg = handle_update_note(["Luna", "old", "New updated note"], book)
    assert "updated" in msg.lower()

    record = book.find("luna")
    assert record.notes[0].value == "new updated note"


def test_update_note_not_found(book):
    handle_add_contact(["ginny", "+380968303034"], book)
    handle_add_note(["ginny", "Text", ""], book)

    msg = handle_update_note(["ginny", "note", "New text"], book)
    assert "No matching note was found" == msg
    

def test_change_tag(book):
    handle_add_contact(["Neville", "+380507777777"], book)
    handle_add_note(["Neville", "Herbology class", "plant"], book)

    msg = handle_change_tag(["Neville", "herbology", "plant", "flower"], book)
    assert "updated" in msg.lower()

    record = book.find("neville")
    assert "flower" in record.notes[0].tags
    assert "plant" not in record.notes[0].tags


def test_delete_note(book):
    handle_add_contact(["Draco", "+380509876543"], book)
    handle_add_note(["Draco", "Slytherin rules", "house"], book)

    msg = handle_delete_note(["Draco", "slytherin"], book)
    assert "deleted" in msg.lower()

    record = book.find("draco")
    assert len(record.notes) == 0


def test_delete_tag(book):
    handle_add_contact(["Sirius", "+380505555555"], book)
    handle_add_note(["Sirius", "Order of Phoenix", "order phx"], book)

    msg = handle_delete_tag(["Sirius", "order", "phx"], book)
    assert "tag was deleted" in msg.lower()

    record = book.find("sirius")
    assert "phx" not in record.notes[0].tags


def test_find_notes_by_tag(book, capsys):
    handle_add_contact(["Fred", "+380505551234"], book)
    handle_add_note(["Fred", "Prank 1", "fun"], book)
    handle_add_note(["Fred", "Prank 2", "fun chaos"], book)

    handle_find_notes_by_tag(["Fred", "fun"], book)

    captured = capsys.readouterr()
    assert "Prank" in captured.out
    assert "fun" in captured.out


def test_show_contact_notes(book, capsys):
    handle_add_contact(["George", "+380505551234"], book)
    handle_add_note(["George", "Joke idea", "fun"], book)

    handle_show_contact_notes(["George"], book)

    captured = capsys.readouterr()
    assert "Joke idea" in captured.out