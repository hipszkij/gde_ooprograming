from Student import Student

student1 = Student("András", "1")
student2 = Student("Tamás", "2")

student1.score = 20
print(student1.passed())

student2.score = 90
print(student2.passed())


