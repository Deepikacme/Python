from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class PDFFile(FileHandler):
    def read(self):
        print("Reading PDF file")

class TextFile(FileHandler):
    def read(self):
        print("Reading Text file")

files = [PDFFile(), TextFile()]

for file in files:
    file.read()