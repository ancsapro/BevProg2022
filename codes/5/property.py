class Szuperhos:
    def __init__(self, nev, szuperero=50):
        self._nev = nev 
        self._szuperero = szuperero

    @property
    def szuperero(self):            # get property
        return self._szuperero

    @szuperero.setter
    def szuperero(self, ertek):     # set property
        self._szuperero = ertek

# === példányosítás ===

hos1 = Szuperhos("Thor", 70)
hos1.szuperero = 100                  # set property hívás
print(hos1.szuperero)                 # get property hívás