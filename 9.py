f = open("students.txt", "r")

lines = f.readlines()

for line in lines[:5]:
    print(line.strip())
f.close()