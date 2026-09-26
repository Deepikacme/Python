try:
    f = open("numbers.txt", "r")

    for line in f:
        try:
            print(int(line))
        except ValueError:
            print("Invalid number")

    f.close()

except FileNotFoundError:
    print("File not found")