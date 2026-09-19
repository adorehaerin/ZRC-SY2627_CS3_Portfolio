class Student:
    def __init__(self, name: str):
        self.name = name


class Course:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)


student1 = Student("Veniz")
student2 = Student("Zoi")
student3 = Student("Bliss")

course = Course("Python Programming")

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

print("Course:", course.name)
print("Students:")

for student in course.students:
    print(student.name)
