import datetime


def get_upcoming_birthdays(users):
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=7)
    upcoming_birthdays = []

    for user in users: # Loop through each user in the provided list of users
        birthday = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday = birthday.replace(year=today.year)

        if birthday < today: # If the birthday has already occurred this year, set it to next year
            birthday = birthday.replace(year=today.year + 1)

        if today <= birthday <= end_date: # Check if the birthday falls within the next 7 days
            congratulation_date = birthday

            if congratulation_date.weekday() >= 5: # If the birthday falls on Saturday (5) or Sunday (6), move the congratulation date to the next Monday
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += datetime.timedelta(days=days_to_monday)

            upcoming_birthdays.append({ # Add the user's name and the adjusted congratulation date to the list of upcoming birthdays
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d'),
            })

    return upcoming_birthdays
