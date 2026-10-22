import datetime


def birthday_in_year(birthday, year):
    try:
        return birthday.replace(year=year)
    except ValueError: # February 29 does not exist in a non-leap year
        return birthday.replace(year=year, day=28) # Use February 28 instead


def get_congratulation_date(birthday):
    if birthday.weekday() >= 5: # If the birthday falls on Saturday (5) or Sunday (6), move the congratulation date to the next Monday
        days_to_monday = 7 - birthday.weekday()
        return birthday + datetime.timedelta(days=days_to_monday)
    return birthday


def get_upcoming_birthdays(users):
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=7)
    upcoming_birthdays = []
    

    for user in users: # Loop through each user in the provided list of users
        birthday = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        # Find the nearest birthday whose congratulation is not in the past.

        for year in (today.year - 1, today.year, today.year + 1):
            upcoming_birthday = birthday_in_year(birthday, year)
            congratulation_date = get_congratulation_date(upcoming_birthday)
            if congratulation_date >= today:
                break

        if upcoming_birthday <= end_date: # Check if the birthday falls within the next 7 days (or was on the weekend just before today's Monday)
            upcoming_birthdays.append({ # Add the user's name and the adjusted congratulation date to the list of upcoming birthdays
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d'),
            })

    return upcoming_birthdays
