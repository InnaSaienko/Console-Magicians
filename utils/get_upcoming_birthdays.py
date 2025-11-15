from datetime import date, timedelta
from typing import Dict, Any

def adjust_for_weekend(num_day):
    if num_day == 5:
        return 2
    elif num_day == 6:
        return 1
    return 0


def get_birthdays(data: Dict[str, Any], days: int = 7) -> list[str]:
    today = date.today()
    upcoming_birthdays = []
    end_date = today + timedelta(days=days)

    for record in data.values():
        if record.birthday and record.birthday.value:
            bd_date_obj = record.birthday.value 
            birthday_this_year = bd_date_obj.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = bd_date_obj.replace(year=today.year + 1) 
            
            diff_days = (birthday_this_year - today).days
            if 0 <= diff_days <= 7:
                weekday = birthday_this_year.weekday()
                birthday_this_year += timedelta(days=adjust_for_weekend(weekday))
            
            if today <= birthday_this_year <= end_date:
                upcoming_birthdays.append(record.name.value)

    return upcoming_birthdays