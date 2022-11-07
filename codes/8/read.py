# a be.txt fájl megnyitása olvasásra
file = open("be.txt", "r", encoding="UTF-8")

# a teljes fájl tartalmának beolvasása
tartalom = file.readlines()

# a tartalom kiíratása soronként
for sor in tartalom:
    sor = sor.rstrip()      # sorvége-jel eltávolítása
    print(sor)

# a megnyitott fájl lezárása
file.close()
