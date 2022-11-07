try:
    file = open("ki.txt", "r")
    tartalom = file.readlines()

    for sor in tartalom:
        sor = sor.rstrip()
        print(sor)

    file.close()
except FileNotFoundError as fnfe:
    print("A fájl nem található!")
