try:
    age=int(input("enter your age:"))
    if age<18:
        raise ValueError("age must be 18 or above")
except ValueError as e:
    print("error",e)
else:
     print("you are eligible")