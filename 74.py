import csv

f = open("students.csv", "r")

reader = csv.reader(f)
next(reader)

sid = input("Enter ID: ")

for row in reader:
    if row[0] == sid:
        print("Student found:", row)

f.close()