def write():
    with open ("demo2.txt","a") as f:
        f.write("I love SRK \n")


def show():
    f = open("demo2.txt")
    print(f.read())
    f.close()

while True:
    print("1. Write.")
    print("2. Display")
    choice = int(input("Enter the choice => "))
    match choice:
        case 1:
            write()
        case 2:
            show()
        case _:
            print("Invalid operation.")