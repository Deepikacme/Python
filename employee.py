class Employee:
    def work(self):
        print("Employee works")
class Manager(Employee):
    pass
m = Manager()
m.work()