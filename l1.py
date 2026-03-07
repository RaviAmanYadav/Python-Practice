# asking user's to add or delete student


def add_student():
    student_name = input("Enter the name of the student=>")
    return student_name


def remove_student(name):
    stu.remove(name)


stu = []
while True:
    print("1. Add student.")
    print("2. Remove student.")
    print("3. Exit")
    print("4. Show student list.")
    choice = int(input("Enter your choice => "))
    match choice:
        case 1:
            stu.append(add_student())
        case 2:
            name = input("Enter the name of the student => ")
            if name in stu:
                remove_student(name)
            else:
                print("Student name is not present.")
        case 3:
            exit()
        case 4:
            print(stu)
        case _:
            print("Invalid option! Please choose the correct options.")
