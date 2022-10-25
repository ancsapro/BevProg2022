def ugat(nev):
    print(nev + ": Vao")

class Kutya:
    def __init__(self, nev, kor):
        self.nev = nev
        self._kor = kor

    @property
    def kor(self):
        return self._kor

    @kor.setter
    def kor(self, ertek):
        self._kor = ertek

    def __str__(self):
        return self.nev + " egy kutya, aki " + str(self._kor*7) + " éves."

    def __eq__(self, masik_kutya):
        return self.nev ==kutya.nev and self.kor == masik_kutya._kor

if __name__ == '__main__':
    kutya = Kutya("Blöki", 2)
    kutya2 = Kutya("Kutya", 1)
    print(kutya)
    print(kutya2)
    print(kutya == kutya2)
    try:
        kutya2.kor = 0
        print(kutya.kor / kutya2.kor)
    except ZeroDivisionError:
        print("ZeroDivisionError Occurred and Handled")
    kutya3 = Kutya("Kutya3", 1)
    kutyak = []

    kutyak.append(kutya.nev)
    kutyak.append(kutya2.nev)
    kutyak.append(kutya3.nev)
    print(kutyak)
    if None:
        print("x")
    else:
        for i in kutyak:
            print(ugat(i))
