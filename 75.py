import csv

f = open("students.csv", "r")
rows = list(csv.reader(f))
f.close()

sid = input("Enter ID: ")
marks = input("Enter new marks: ")

for row in rows:
    if row[0] == sid:
        row[3] = marks

f = open("students.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(rows)
f.close()

print("Marks updated")