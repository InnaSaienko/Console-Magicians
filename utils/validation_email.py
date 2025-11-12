import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def validation_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email, re.IGNORECASE) is not None
