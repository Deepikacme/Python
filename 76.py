import csv

f = open("students.csv", "r")
rows = list(csv.reader(f))
f.close()

sid = input("Enter ID to delete: ")

f = open("students.csv", "w", newline="")
writer = csv.writer(f)

for row in rows:
    if row[0] != sid:
        writer.writerow(row)

f.close()

print("Student deleted")