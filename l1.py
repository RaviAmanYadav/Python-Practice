# asking user's to add or delete student


def add_student():
    student_name = input("Enter the name of the student=>")
    return student_name

def remove_student(name):
    stu.remove(name)
    

stu = []
while True:
    print("1. Add student")
    print("3. Exit")
    choice = int(input("Enter your choice => "))
    match choice:
        case 1:
            stu.append(add_student())
        case 3:
            exit()
        case 4:
            print(stu)
        case _:
            print("Invalid option! Please choose the correct options.")
