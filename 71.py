import csv

f = open("students.csv", "w", newline="")

writer = csv.writer(f)

writer.writerow(["ID", "Name", "Course", "Marks"])
writer.writerow([1, "Deepika", "CME", 85])
writer.writerow([2, "Priya", "CSE", 78])
writer.writerow([3, "Rahul", "EEE", 90])

f.close()

print("CSV file created")