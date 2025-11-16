from datetime import datetime


def validation_birthday(value: str) -> bool:
    try:
        # parsing wrong string will raise an error if format is not suitable.
        datetime.strptime(value, "%d.%m.%Y")
        return True
    except Exception:
        return False
