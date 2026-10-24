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


x = [4,1,2,3]
y = sorted(x)
x.sort()

sorted(x, reverse=True)
sorted([-4,1,-2,3],key=abs)

# [1,-2,3,-4]
rijeci= ["cao","pozdrav","hello"]
print(sorted(rijeci, key=len))



#####
imena = ["Ana","Emir"]
god = [20, 22]

print(list(zip(imena, god)))


## zadatak 2
studenti = ["Amra","Emir","Lejla","Tarik","Ana"]
bodovi = [78,92,65,88,92]

print(list(zip(studenti, bodovi)))



for i in range(len(studenti)):
    if(bodovi[i]>=80):
        print(f"Student: {studenti[i]}, bodovi:{bodovi[i]}")



def dodaj(zadaci, naziv, prioritet=2):
    if naziv == "":
        print("naziv ne moze biti prazan")
        return
    zadaci.append({"naziv":naziv})

def prikazi(zadaci):
    for i, z in enumerate(zadaci, start=1):
        oznaka = "x" if z["gotovo"] else " "
        print(f"{i}, [{oznaka}]")