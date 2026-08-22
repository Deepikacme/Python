class Calcu:
    def add(self,a,b,c):
        return a+b+c
obj=Calcu()
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
print("Sum =",obj.add(a,b,c))