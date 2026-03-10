
class Parent:
    def __init__(self, father_name,mother_name):
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


    def add_student(roll_number):
        student_name = input("Enter the name of the student => ")
        student_age = input("Enter student age => ")
        student_father_name = input("Enter the name of student's father => ")
        student_mother_name = input("Enter the name of student's mother => ")

        student_details = {
            "roll": roll_number,
            "name": student_name,
            "age": student_age,
            "father": student_father_name,
            "mother": student_mother_name,
        }

        return student_details

    def remove_student(roll_number):
        if roll_number in stu:
            del stu[roll_number]
            print("Student record has been removed.")
        else:
            print("Roll number doesn't exit! Please enter valid roll number.")


    def update_student_details():

        while True:
            roll_number = int(input("Enter the roll number for updatation => "))
            if roll_number in stu:
                print("Enter new details.")
                name = input("Enter name of the student => ")
                stu[roll_number]["name"] = name
                print("Student details has been updated.")
                break
            else:
                print("Roll number not found! Please enter correct roll number")

    while True:
        print("1. Add studnet.")
        print("2. Remove student.")
        print("3. Show all student details.")
        print("4. Update student's details.")
        print("5. Exit.")

        choice = int(input("Choose the option =>"))

        match choice:
            case 1:
                student = add_student(roll_numeber)
                stu[roll_numeber] = student
                roll_numeber += 1
            case 2:
                roll_number = int(input("Enter the roll number to be removed => "))
                remove_student(roll_number)
            case 3:
                for roll_number, details in stu.items():
                    print("\nRoll number : ", roll_number)
                    for key, value in details.items():
                        print(f"{key} : {value}")
            case 4:
                update_student_details()
            case 5:
                exit()
            case _:
                print("Please choose the correct option.")




