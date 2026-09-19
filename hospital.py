class Doctor:
    def show(self):
        print("Doctor")
class Patient:
    def show(self):
        print("Patient")
class Hospital:
    def __init__(self):
        self.doctor = Doctor()
        self.patient = Patient()
h = Hospital()
h.doctor.show()
h.patient.show()