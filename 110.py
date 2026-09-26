filename = "data.txt"

while True:
    print("\n1. Write")
    print("2. Read")
    print("3. Append")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        data = input("Enter data: ")
        f = open(filename, "w")
        f.write(data)
        f.close()
        print("Data written")

    elif choice == "2":
        f = open(filename, "r")
        print(f.read())
        f.close()

    elif choice == "3":
        data = input("Enter data: ")
        f = open(filename, "a")
        f.write("\n" + data)
        f.close()
        print("Data appended")

    elif choice == "4":
        print("Program ended")
        break

    else:
        print("Invalid choice")