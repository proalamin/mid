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


    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f"{self.name} has been enrolled successfully.")
        else:
            print(f"{self.name} is already enrolled.")

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print(f"{self.name} has been dropped.")
        else:
            print(f"{self.name} is not enrolled.")

    def view_student_info(self):
        if self.is_enrolled:
            status = "True"
        else:
            status = "False"
        print(f"Student ID: {self.student_id}, Name: {self.name}, Department: {self.department}, Status: {status}")


# Menu System
def menu():
    while True:
        print("---> Student Management System <---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        option = input("enter your option (1-4): ")

        if option == "1":
            if not StudentDatabase.student_list:
                print("No students available now")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()
        




s1 = Student(1, "Rahim", "EEE")
s2 = Student(2, "Karim", "CSE")


s1.enroll_student()
# s2.enroll_student()

# s2.drop_student()

# s1.view_student_info()
# s2.view_student_info()

menu()