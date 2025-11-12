import re

def validation_phone(phone: str) -> str | ValueError:
    formatted_phone_number = re.sub(r"[^\d+]", "", phone)
    return formatted_phone_number
