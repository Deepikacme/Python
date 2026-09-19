class Printer:
    def print_data(self):
        print("Printing student details")
class Student:
    def print_details(self, printer):
        printer.print_data()
s = Student()
s.print_details(Printer())