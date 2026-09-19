class Person:
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Course:
    pass

class CertificateService:
    def generate(self):
        print("Certificate generated")

class LearningSystem:
    def __init__(self):
        self.student = Student()
        self.teacher = Teacher()
        self.course = Course()

    def certificate(self, service):
        service.generate()

LearningSystem().certificate(CertificateService())