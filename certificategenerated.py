class CertificateGenerator:
    def generate(self):
        print("Certificate generated")
class Course:
    def certificate(self, generator):
        generator.generate()
Course().certificate(CertificateGenerator())