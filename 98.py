filename = input("Enter filename: ")

try:
    f = open(filename, "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File does not exist")