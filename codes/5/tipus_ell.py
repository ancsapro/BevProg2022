class Szuperhos:
    def __init__(self, nev, szuperero=50):
        self._nev = nev 
        self._szuperero = szuperero

    # ...

    def __add__(self, masik_hos):
        if isinstance(masik_hos, Szuperhos):   # típusellenőrzés
            uj_szuperero = self._szuperero + masik_hos._szuperero
            uj_szuperhos = Szuperhos("Megahős", uj_szuperero)
            return uj_szuperhos
        else:
            print("Egy szuperhőst csak egy másik szuperhőssel lehet összeadni.")