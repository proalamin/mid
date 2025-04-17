class StudentDatabase:
    student_list=[]


    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:

    def __init__(self, student_id, name, department):
        self.student_id =student_id
        self.name= name
        self.department = department
        self.is_enrolled = False

        StudentDatabase.add_student(self)

s1 = Student(1, "Rahim", "EEE")
s2 = Student(2, "Karim", "CSE")




