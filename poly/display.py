class A:
    def display(self):
        print("One")

class B(A):
    def display(self):
        print("One Two")

obj=B()
obj.display()