class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, newScore):
        self._score = newScore

    def success(self):
        if self._score >= 60:
            print("igen")
        else:
            print("nem")


student = Student(1, "Teszt", 50)
student.success()

student.score = 80
student.success()

