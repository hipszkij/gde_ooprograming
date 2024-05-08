from Animal import Animal


class Cat(Animal):
    def __init__(self, name, kor, fajta, szin):
        self._szin = szin
        print("Cat constructor")

    def speak(self):
        print("Cat is speaking")

    def tostring(self):
        print(f"A nevem {self._nev}")
        print(f"A korom {self._kor}")
        print(f"A fajtám {self._fajta}")
        print(f"A szinem {self._szin}")

    def my_name(self):
        print(f"A macska neve: {self._nev}")
