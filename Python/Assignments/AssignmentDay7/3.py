from datetime import datetime

def days_until_birthday(birthday):
    today = datetime.now()
    next_birthday = birthday.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_until = (next_birthday - today).days
    return days_until


birthday = datetime.strptime("2002-10-22", "%Y-%m-%d")

days = days_until_birthday(birthday)
print(f"Days until your next birthday: {days}")
