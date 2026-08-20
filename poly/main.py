from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------- Functions ----------

def add_student():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, roll_no, branch, phone) VALUES(?,?,?,?)",
        (
            name_entry.get(),
            roll_entry.get(),
            branch_entry.get(),
            phone_entry.get()
        )
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Added Successfully")

    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    branch_entry.delete(0, END)
    phone_entry.delete(0, END)

# ---------- GUI ----------

root = Tk()
root.title("Student Management System")
root.geometry("400x350")

Label(root, text="Student Management System", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Name").pack()
name_entry = Entry(root, width=30)
name_entry.pack()

Label(root, text="Roll Number").pack()
roll_entry = Entry(root, width=30)
roll_entry.pack()

Label(root, text="Branch").pack()
branch_entry = Entry(root, width=30)
branch_entry.pack()

Label(root, text="Phone").pack()
phone_entry = Entry(root, width=30)
phone_entry.pack()

Button(root, text="Add Student", command=add_student, bg="green", fg="white").pack(pady=20)

root.mainloop()