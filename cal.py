def add():
    a = int(input("Enter value A =>"))
    b = int(input("Enter value B =>"))
    return a + b


def sub():
    a = int(input("Enter value A =>"))
    b = int(input("Enter value B =>"))
    return a - b


def mul():
    a = int(input("Enter value A =>"))
    b = int(input("Enter Value B =>"))
    return a * b


def div():
    a = int(input("Enter value A=>"))
    b = int(input("Enter value B=>"))
    return a / b


def mod():
    a = int(input("Enter value A=>"))
    b = int(input("Enter value B=>"))
    return a % b


choice = 0

while choice != 6:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modular")
    print("6. Exit")
    choice = int(input("Enter your choice => "))

    match choice:
        case 1:
            print("Sum =", add())
        case 2:
            print("Sub =", sub())
        case 3:
            print("Multiplication =>", mul())
        case 4:
            print("Division =", div())
        case 5:
            print("Modular =>", mod())
        case 6:
            exit()
        case _:
            print("Invalid option not present here!!!")
