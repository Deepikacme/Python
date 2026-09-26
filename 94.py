import os

if os.path.exists("data.txt"):
    f = open("data.txt", "r")
    print(f.read())
    f.close()
else:
    print("File does not exist")