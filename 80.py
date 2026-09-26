import csv

f = open("students.csv", "r")

reader = csv.reader(f)
header = next(reader)
rows = list(reader)

f.close()

rows.sort(key=lambda x: int(x[3]), reverse=True)

f = open("sorted_students.csv", "w", newline="")

writer = csv.writer(f)
writer.writerow(header)
writer.writerows(rows)

f.close()

print("Students sorted successfully")