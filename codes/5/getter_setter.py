class Szuperhos:
    def __init__(self, nev, szuperero=50):
        self._nev = nev 
        self._szuperero = szuperero

    def get_szuperero(self):          # getter metódus
        return self._szuperero

    def set_szuperero(self, ertek):   # setter metódus
        self._szuperero = ertek

# === példányosítás ===

hos1 = Szuperhos("Thor", 70)
hos1.set_szuperero(100)               # setter hívás
print(hos1.get_szuperero())           # getter hívás