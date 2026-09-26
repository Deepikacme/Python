import os

if not os.path.exists("newfile.txt"):
    f = open("newfile.txt", "w")
    f.write("New File")
    f.close()
    print("File created")
else:
    print("File already exists")
