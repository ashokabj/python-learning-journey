class Student:
    def __init__(self, marks):
        self.__marks = marks


    @property
    def marks(self):
        return self.__marks

student = Student(85)

print(student.marks)