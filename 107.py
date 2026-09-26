import csv

f = open("attendance.csv", "w", newline="")

writer = csv.writer(f)

writer.writerow(["Name", "Attendance"])
writer.writerow(["Deepika", "Present"])
writer.writerow(["Priya", "Absent"])

f.close()

print("Attendance saved")