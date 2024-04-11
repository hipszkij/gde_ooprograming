from Poligon import Poligon

class Teglalap(Poligon):
    def __init__(self, a, b):
        super().__init__(a, b)

    def kerulet(self):
        return 2 * (self._a + self._b)

    def terulet(self):
        return self._a * self._b