# creating files and writing it 
with open("demofile.txt", "a") as f:
    f.write("I am learning python.")
f.close()

# reading files here
with open("demofile.txt") as f:
    print(f.read())
f.close()
