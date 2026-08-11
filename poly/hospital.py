class Hospital:
    def services(self):
        print("Hospital provides general medical services")
class SpecializedHospital(Hospital):
    def services(self):
        print("Specialized Hospital provides specialized treatments")
hospital=Hospital()
specialized=SpecializedHospital()
hospital.services()
specializes=SpecializedHospital()