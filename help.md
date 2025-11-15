# 📒 Bot Commands Guide

## 👥 Contact Management

| Command | Usage | Description |
|---------|--------|-------------|
| **add-contact** | `add-contact [name] [phone] [email]` | Adds a new contact or updates existing one with specified phone and email. |
| **add-birthday** | `add-birthday [name] [birthday date]` | Adds a birthday date to a contact. Format: `DD.MM.YYYY`. |
| **update-phone** | `update-phone [name] [old phone] [new phone]` | Updates a contact's phone number. |
| **show-birthday** | `show-birthday [name]` | Displays the birthday date of the specified contact. |
| **upcoming-birthdays** | `upcoming-birthdays` | Shows contacts with birthdays occurring within the next 7 days. |
| **add-address** | `add-address [name] ["user address"]` | Adds or updates a contact's address. |
| **find-contact** | `find-contact [name]` | Displays full contact information including phone, email, address, birthday, notes, etc. |
| **delete-contact** | `delete-contact [name]` | Removes the contact from the address book. |
| **show-phone** | `show-phone [name]` | Shows all stored phone numbers for the contact. |
| **all-contact** | `all-contact` | Shows a full list of all contacts. |

---

## 📝 Notes Management

| Command | Usage | Description |
|---------|--------|-------------|
| **add-note** | `add-note [name] ["note"] ["tag tag ..."]` | Adds a note with one or more tags to a contact. |
| **show-contact-notes** | `show-contact-notes [name]` | Displays all notes of the specified contact. |
| **delete-note** | `delete-note [name] ["keyword"]` | Removes notes containing the specified keyword. |
| **update-note** | `update-note [name] ["keyword"] ["new note"]` | Updates note text found by keyword. |
| **find-notes-by-tag** | `find-notes-by-tag [name] [tag]` | Shows notes filtered by tag. |

---

## 🏷️ Tags Management

| Command | Usage | Description |
|---------|--------|-------------|
| **add-tag** | `add-tag [name] ["keyword"] [tag]` | Adds a tag to a specific note. |
| **change-tag** | `change-tag [name] ["keyword"] [old tag] [new tag]` | Replaces an existing tag with another. |
| **delete-contact-tag** | `delete-contact-tag [name] ["keyword"] ["tag"]` | Removes a tag from a note. |

---

## 🤖 Other Commands

| Command | Usage | Description |
|---------|--------|-------------|
| **hello** | `hello` | Displays a welcome message. |
| **close / exit** | `close` / `exit` | Ends the program. |
| **help** | `help` | Shows a list of available commands. |

---
