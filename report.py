class ReportGenerator:
    def generate(self):
        print("Report generated")
class Employee:
    def report(self, generator):
        generator.generate()
Employee().report(ReportGenerator())