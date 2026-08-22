from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def process(self):
        pass

    def display(self):
        print("File:", self.filename)


class PDFHandler(FileHandler):
    def process(self):
        print("Processing PDF file")


class CSVHandler(FileHandler):
    def process(self):
        print("Processing CSV file")


class ExcelHandler(FileHandler):
    def process(self):
        print("Processing Excel file")


class JSONHandler(FileHandler):
    def process(self):
        print("Processing JSON file")


files = [
    PDFHandler("document.pdf"),
    CSVHandler("data.csv"),
    ExcelHandler("report.xlsx"),
    JSONHandler("data.json")
]

for file in files:
    file.display()
    file.process()
    print()