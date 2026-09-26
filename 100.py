try:
    filename = input("Enter filename: ")

    f = open(filename, "w")
    data = input("Enter data: ")
    f.write(data)
    f.close()

    f = open(filename, "r")
    print("File contents:", f.read())
    f.close()

    print("File operation completed")

except Exception as e:
    print("Error:", e)