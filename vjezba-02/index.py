import random
from datetime import date, timedelta
from collections import Counter

def testBirthdays():
    startOfYear = date(2026, 1, 1)
    birthdays = []

    dani = random.randint(0, 364)
    birthday = startOfYear + timedelta(days=dani)
    birthdays.append(birthday)



    if len(birthdays) == len(set(birthdays)):
        return None


testBirthdays()




########################


def analyze_birthdays():
    with open("real_birthdays.txt", "r") as file:
        birthdays = [line.strip() for line in file if line.strip()]

    counts = Counter(birthdays)

    print("Ukupno rodjendana:", len(birthdays))
    print("Jedinstvenih rodenana:", len(counts))
    print("Postoje duplikati:", len(birthdays) != len(counts))

    print("\nDatumi koji se ponavljaju:")
    for datum in sorted(d for d in counts if counts[d] > 1):
        print(datum, "-", counts[datum], "puta")

    probability = 1

    for i in range(38):
        probability *= (365 - i) / 365

    probability = (1 - probability) * 100

    print("\nTeorijska vjerovatnoca poklapanja za 38 osoba:",
          round(probability, 2), "%")

    print("Stvarno poklapanje postoji:", len(birthdays) != len(counts))


analyze_birthdays()

