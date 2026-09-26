username = input("Enter username: ")
password = input("Enter password: ")

f = open("users.txt", "w")
f.write(username + "," + password)
f.close()

print("Registration successful")

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login successful")
else:
    print("Invalid login")