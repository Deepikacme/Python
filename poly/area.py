class Area:
 def calculate(self,a,b=0):
        if b==0:
            print("Area of Square =",a*a)
            print("Area of Circle =",3.14*a*a)
        else:
            print("Area of Rectangle =",a*b)
obj=Area()
obj.calculate(5)    
obj.calculate(10,20,30)  