f = open("students.txt", "r")

sid = input("Enter ID: ")

for line in f:
    if line.startswith(sid + ","):
        print("Student found:", line.strip())

f.close()