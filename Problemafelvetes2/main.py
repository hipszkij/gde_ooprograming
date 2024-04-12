from Classes.Student import Student
from Classes.Teacher import Teacher
from Classes.Course import Course
from Classes.Grade import Grade


student1 = Student("John Doe", 'S123-456', 'john@example.com')
teacher1 = Teacher("Jane Smith", "T987-111", "Software Enginer")
course1 = Course("OOPROG-N-LA07", "Objectum oriented programing", teacher1)
grade1 = Grade(student1, course1, 3)

