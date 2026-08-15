class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, mark):

        if 0 <= mark <=100:
            self.__marks = mark

        else:
            print("Invalid marks.")

student = Student(85)

print(student.marks)

student.marks = 95
print(student.marks)

student.marks = 120