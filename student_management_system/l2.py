class Parent:
    def __init__(self, father_name, mother_name):
        self.father_name = father_name
        self.mother_name = mother_name


class Student:
    def __init__(self, roll, name, age, parent):
        self.roll = roll
        self.name = name
        self.age = age
        self.parent = parent


class School:
    def __init__(self):
        self.students = {}
        self.roll_number = 1

    # Adding the students.
    def add_student(self):
        name = input("Enter the name of the student => ")
        age = input("Enter student age => ")
        student_father_name = input("Enter the name of student's father => ")
        student_mother_name = input("Enter the name of student's mother => ")
        parent = Parent(student_father_name, student_mother_name)
        student = Student(self.roll_number, name, age, parent)
        self.students[self.roll_number] = student
        print("Student add successfully")
        self.roll_number += 1

    # deletion of a students
    def remove_student(self):
        roll_number = int(input("Enter the roll number to be removed => "))
        if roll_number in self.students:
            del self.students[roll_number]
            print("Student record has been removed.")
        else:
            print("Roll number doesn't exit! Please enter valid roll number.")

    # Updation of students
    def update_student_details(self):

        while True:
            roll_number = int(input("Enter the roll number for updatation => "))
            if roll_number in self.students:
                print("Enter new details.")
                name = input("Enter name of the student => ")
                self.students[roll_number].name = name
                print("Student details has been updated.")
                break
            else:
                print("Roll number not found! Please enter correct roll number")

    def show_student(self):
        if not self.students:
            print("No students are present.")
            return

        for roll_number, students in self.students.items():
            print("Roll number => ", roll_number)
            print("Name : ", students.name)


school = School()

while True:
    print("1. Add studnet.")
    print("2. Remove student.")
    print("3. Show all student details.")
    print("4. Update student's details.")
    print("5. Exit.")

    choice = int(input("Choose the option =>"))

    match choice:
        case 1:
            school.add_student()
        case 2:
            school.remove_student()
        case 3:
            school.show_student()
        case 4:
            school.update_student_details()
        case 5:
            exit()
        case _:
            print("Please choose the correct option.")
