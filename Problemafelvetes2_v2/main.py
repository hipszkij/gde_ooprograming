from Classes.Student import Student
from Classes.Teacher import Teacher
from Classes.Course import Course
from Classes.Grade import Grade

#Létrehozzuk a tanár objektumot
teacher1 = Teacher("Jane Smith", "T987-111", "Software Enginer")
#Létehozzuk a kurzus objektumot
course1 = Course("OOPROG-N-LA07", "Objectum oriented programming", teacher1)

#Létrehozunk három különböző diákot, más más érdemjeggyel
student1 = Student("John Doe", 'S123-456', 'john.doe@example.com')
grade1 = Grade(student1, course1, 3)

student2 = Student("John Eve", 'S123-457', 'john.eve@example.com')
grade2 = Grade(student1, course1, 1)

student3 = Student("Marta Boo", 'S123-458', 'marta.boo@example.com')
grade3 = Grade(student1, course1, 5)

#Listába rakom a létrehozott diákokat
gradeList = {
    Grade(student1, course1, 3),
    Grade(student2, course1, 1),
    Grade(student3, course1, 5)
}

sumGrade = 0

for grade in gradeList:
    sumGrade += grade._student._study_average


print(sumGrade)