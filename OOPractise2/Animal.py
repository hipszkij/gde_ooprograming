class Animal:
    def __init__(self, name, kor, fajta):
        self._nev = name
        self._kor = kor
        self._fajta = fajta
        print("Allat konstruktor")

    def tostring(self):
        print(f"A nevem {self._nev}")
        print(f"A korom {self._kor}")
        print(f"A fajtám {self._fajta}")

    def my_name(self):
        print(f"A nevem {self._nev}")

    def speak(self):
        print("Animal is speaking")
        
