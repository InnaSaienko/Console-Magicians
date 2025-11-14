import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

def validation_phone(phone: str) -> str | ValueError:
    try:
        phone_number_obj = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(phone_number_obj):
            raise ValueError
        formatted_phone_number = phonenumbers.format_number(
            phone_number_obj, phonenumbers.PhoneNumberFormat.E164
        )
        return formatted_phone_number
    except NumberParseException:
        raise ValueError
