from datetime import date, timedelta


def adjust_for_weekend(num_day):
    if num_day == 5:
        return 2
    elif num_day == 6:
        return 1
    return 0


def get_birthdays(data) -> list[dict]:
    today = date.today()
    upcoming_birthdays = []

    for record in data.values():
        birthday = record.birthday
        if not birthday:
            continue

        congratulation_date = birthday.value.replace(year=today.year)

        if congratulation_date < today:
            congratulation_date = congratulation_date.replace(year=congratulation_date.year + 1)

        diff_days = (congratulation_date - today).days

        if 0 <= diff_days <= 7:
            weekday = congratulation_date.weekday()
            congratulation_date += timedelta(adjust_for_weekend(weekday))

            upcoming_birthdays.append({
                "name": record.name.value,
                "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
            })

    return upcoming_birthdays