try:
    x=int(input("enter x value"))
    y=int(input("enter y value"))
    z=x/y
    print(z)
    print("end program")
    print("rest of the lines")
except ZeroDivisionError:
    print("Error")
