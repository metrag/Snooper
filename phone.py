import re
import phonenumbers
from phonenumbers import geocoder, carrier

def validate_phone_number(phone_number):
    phone_number = phone_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    if phone_number.startswith("8"):
        phone_number = "+7" + phone_number[1:]
    elif phone_number.startswith("7"):
        phone_number = "+" + phone_number
    elif not phone_number.startswith("+"):
        phone_number = "+" + phone_number

    if len(phone_number) == 12 and phone_number[1:].isdigit():
        return phone_number
    else:
        return None
    
def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, "ru")
        phone_carrier = carrier.name_for_number(parsed_number, "ru")

        return {
            "country": country,
            "carrier": phone_carrier,
        }
    except phonenumbers.NumberParseException:
        return {"error": "Некорректный номер телефона"}