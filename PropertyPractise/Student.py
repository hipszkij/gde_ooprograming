class Student:

    def __init__(self, name, id, score=0):
        self.name = name
        self.id = id
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, newScore):
        self._score = newScore

    def passed(self):
        if self._score >= 60:
            return "Teljesítette"
        else:
            return "Nem teljesítette"

