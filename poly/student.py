class Student:
    def introduce(self):
        print("Hi,I am a Student.")  
class Employee:
    def introduce(self):
        print("Hi,I am an Employee.")
def introduce_person(person):
    person.introduce()
s=Student()
e=Employee()
introduce_person(s)
introduce_person(e)