ime = input("Kako se zoves?: ")
godine = int(input("Koliko imas godina: "))

print(f"Pozdrav {ime}, ti imas {godine} godina, a 2030. ces imati {(2030 - 2026) + godine}")

sekunde = int(input("Unesi broj sekundi"))

sati = sekunde // 3600
preostale_sekunde = sekunde % 3600
minute = preostale_sekunde // 60
konacne_sekunde = preostale_sekunde % 60

print(f"{sekunde} sekundi je tačno: {sati}h {minute}m {konacne_sekunde}s")




## Ocjene

ocjene = [8,6,10,7,9,6,8]
print(f"Prva ocjena je {ocjene[0]} a. zadnja je {ocjene[-1]}")
