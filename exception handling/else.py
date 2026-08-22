try:
    num=int(input("enter first number"))
    num=int(input("enter secound number"))
    res=num
except ValueError:
    print("please enter valid numbers:")
except ZeroDivisionError:
    print("div by zero is not allowed")
else:
    print("division:",2)


