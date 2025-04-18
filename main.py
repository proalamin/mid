class StudentDatabase:
    student_list=[]


    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"{self.__name} has been enrolled successfully.")
        else:
            print(f"{self.__name} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} has been dropped.")
        else:
            print(f"{self.__name} is not enrolled.")

    def view_student_info(self):
        if self.__is_enrolled:
            status = "True"
        else:
            status = "False"
        print(f"Student ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Status: {status}")

    def get_student_id(self):
        return self.__student_id


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
        
        elif option == "2":
            print("Fill up this question for enroll-")
            student_id = int(input("Enter the student id: "))
            name = input("Enter the student's name: ")
            department = input("Enter the student's department: ")
            new_student = Student(student_id, name, department)
            new_student.enroll_student()

        elif option == "3":
            print("Fill up this question for drop-")
            student_id = int(input("Enter the student ID: "))
            student_found = False
            for student in StudentDatabase.student_list:
                if student.get_student_id() == student_id:
                    student.drop_student()
                    student_found = True
                    break
            if not student_found:
                print("Student ID not found!")

        elif option == "4":
            print("Logout from the system.")
            break

        else:
            print("Invalid choice. Please try again.")


s1 = Student(1, "Rahim", "EEE")
s2 = Student(2, "Karim", "CSE")

menu()