f = open("students.txt", "r")
lines = f.readlines()
f.close()

sid = input("Enter ID: ")
marks = input("Enter new marks: ")

f = open("students.txt", "w")

for line in lines:
    data = line.strip().split(",")

    if data[0] == sid:
        data[3] = marks

    f.write(",".join(data) + "\n")

f.close()

print("Marks updated")