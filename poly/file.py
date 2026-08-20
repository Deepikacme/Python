class PDFFile:
    def open(self):
        print("Opening PDF file.")
class WordFile:
    def open(self):
        print("Opening Word file.")
def open_file(file):
    file.open()
pdf = PDFFile()
word = WordFile()
open_file(pdf)
open_file(word)