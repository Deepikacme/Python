import csv

f = open("students.csv", "a", newline="")

writer = csv.writer(f)
writer.writerow([4, "Anjali", "CME", 88])

f.close()

print("Student added")