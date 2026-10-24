import random
from datetime import date, timedelta

def testBirthdays():
    startOfYear = date(2026, 1, 1)
    birthdays = []

    dani = random.randint(0, 364)
    birthday = startOfYear + timedelta(days=dani)
    birthdays.append(birthday)



    if len(birthdays) == len(set(birthdays)):
        return None


testBirthdays()


