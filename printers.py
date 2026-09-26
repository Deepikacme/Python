class Printer:
    pass
class Student:
    def print_details(self, p):
        print("Student USES-A Printer")
Student().print_details(Printer())