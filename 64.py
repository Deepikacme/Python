f = open("students.txt", "r")
name = input("Enter name: ")
for line in f:
    if name in line:
        print("Student found:", line.strip())
f.close()