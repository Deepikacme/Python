try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except PermissionError:
    print("Permission denied")