def write():
    with open("demo2.txt", "a") as f:
        text = input("Enter what you want to write => ")
        f.write(text + "\n")


def show():
    with open("demo2.txt","r") as f:
        # print(f.readlines(20))
        lines = f.readlines()
        for i, line in enumerate(lines, 1):
            print(i, "=>", repr(line))

while True:
    print("1. Write.")
    print("2. Display")
    print("3. Exit")
    choice = int(input("Enter the choice => "))
    match choice:
        case 1:
            write()
        case 2:
            show()
        case 3:
            exit()
        case _:
            print("Invalid operation.")
