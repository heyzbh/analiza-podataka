

import time
import os

# Mapa lavirinta
# '#' = zid, ' ' = prazno polje, 'D' = dijamant, 'R' = start robota
lavirint = [
    "##########",
    "#R   #   #",
    "# ## # # #",
    "#  #   # #",
    "## ##### #",
    "#      # #",
    "###### # #",
    "#    #  D#",
    "##########",
]

# pretvaramo svaki red u listu da mozemo mijenjati polja
mapa = [list(red) for red in lavirint]

# Ssmjerovi
smjerovi = {
    ">": (0, 1),   # desno
    "v": (1, 0),   # dole
    "<": (0, -1),  # lijevo
    "^": (-1, 0),  # gore
}

# Sta je desno od kojeg smjera
desno_od = {">": "v", "v": "<", "<": "^", "^": ">"}
# Sta je lijevo od kojeg smjera
lijevo_od = {">": "^", "^": "<", "<": "v", "v": ">"}

# robot na pocetku
robot_red = 0
robot_kolona = 0
for r in range(len(mapa)):
    for k in range(len(mapa[r])):
        if mapa[r][k] == "R":
            robot_red = r
            robot_kolona = k
            mapa[r][k] = " "

robot_smjer = ">"  # robot na pocetku gleda desno


# ---------- SENZORI ----------

def polje_ispred():
    # Vraca znak koji se nalazi na polju ispred robota
    dr, dk = smjerovi[robot_smjer]
    return mapa[robot_red + dr][robot_kolona + dk]


def je_zid():
    # True ako je ispred robota zid
    return polje_ispred() == "#"


def je_dijamant():
    # True ako je ispred robota dijamant
    return polje_ispred() == "D"


# ---------- OKRETANJE ----------

def okreni_desno():
    global robot_smjer
    robot_smjer = desno_od[robot_smjer]


def okreni_lijevo():
    global robot_smjer
    robot_smjer = lijevo_od[robot_smjer]


# ---------- MOZAK ----------

def odluci_smjer():
    # Pravilo desne ruke:
    # 1. Prvo se okreni desno
    # 2. Dok je ispred zid, okreci se lijevo
    # Tako robot nikad ne udari u zid.
    okreni_desno()
    while je_zid():
        okreni_lijevo()


# ---------- KRETANJE I CRTANJE ----------

def idi_naprijed():
    global robot_red, robot_kolona
    dr, dk = smjerovi[robot_smjer]
    robot_red = robot_red + dr
    robot_kolona = robot_kolona + dk


def nacrtaj():
    os.system("cls" if os.name == "nt" else "clear")
    for r in range(len(mapa)):
        red = ""
        for k in range(len(mapa[r])):
            if r == robot_red and k == robot_kolona:
                red = red + robot_smjer
            else:
                red = red + mapa[r][k]
        print(red)


koraci = 0
while True:
    nacrtaj()
    print("Koraci:", koraci)
    time.sleep(0.5)

    odluci_smjer()

    if je_dijamant():
        idi_naprijed()
        koraci = koraci + 1
        mapa[robot_red][robot_kolona] = " "
        nacrtaj()
        print("Robot je nasao dijamant za", koraci, "koraka!")
        break

    idi_naprijed()
    koraci = koraci + 1

    if koraci > 500:
        print("Robot se izgubio :(")
        break