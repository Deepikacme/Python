from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class SalesReport(Report):
    def generate(self):
        print("Generating Sales Report")

class EmployeeReport(Report):
    def generate(self):
        print("Generating Employee Report")

reports = [SalesReport(), EmployeeReport()]

for report in reports:
    report.generate()