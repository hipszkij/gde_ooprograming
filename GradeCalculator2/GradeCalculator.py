class GradeCalculator:
    def __init__(self, testScore, devScore):
        self.testScore = testScore
        self.devScore = devScore

    def getAvg(self):
        return (self.testScore + self.devScore) / 2

    def printGrade(self):
        avg = self.getAvg()

        if avg >= 90:
            return 5
        elif avg >= 80:
            return 4
        elif avg >= 70:
            return 3
        elif avg >= 60:
            return 2
        else:
            return 1

    def __str__(self):
        return f"A tanuló osztályzata: {self.printGrade()}"

    
student1 = GradeCalculator(70, 80)
print(student1)

student2 = GradeCalculator(20, 40)
print(student2)