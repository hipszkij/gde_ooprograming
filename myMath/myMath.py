class myMath:
    def __init__(self):
        pass

    def osszead(self, a, b):
        return self._reszosszead(a, b)

    def _reszosszead(self, a, b):
        return a + b


math = myMath()
osszeg = math.osszead(1, 2)
print(osszeg)

math.
