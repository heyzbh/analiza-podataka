#### Prvi zadatak
ime = input("Kako se zoves?: ")
godine = int(input("Koliko imas godina: "))

print(f"Pozdrav {ime}, ti imas {godine} godina, a 2030. ces imati {(2030 - 2026) + godine}")

sekunde = int(input("Unesi broj sekundi"))

sati = sekunde // 3600
preostale_sekunde = sekunde % 3600
minute = preostale_sekunde // 60
konacne_sekunde = preostale_sekunde % 60

print(f"{sekunde} sekundi je tačno: {sati}h {minute}m {konacne_sekunde}s")




#### Drugi zadatak
ocjene = [8,6,10,7,9,6,8]
print(f"Prva ocjena je {ocjene[0]} a. zadnja je {ocjene[-1]}")

### Treci zadatak
def prosjek(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

## <55 5, 65 6, 75 7, 85 8, 95 9 - ostalo 10

def ocjena(bodovi):
    if bodovi<55:
        return 5
    elif bodovi<65:
        return 6
    elif bodovi<75:
        return 7
    elif bodovi<85:
        return 8
    elif bodovi<95:
        return 9
    else:
        return 10


print(f"Tvoja ocjena je {ocjena(67)}")