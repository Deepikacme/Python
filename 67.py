f = open("students.txt", "r")
lines = f.readlines()
f.close()

sid = input("Enter ID to delete: ")

f = open("students.txt", "w")

for line in lines:
    if not line.startswith(sid + ","):
        f.write(line)

f.close()

print("Record deleted")