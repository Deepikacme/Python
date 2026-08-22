class Duck:
    def talk(self):
        print("Duck says: Quack Quack!")
class Person:
    def talk(self):
        print("Person says: Hello!")
def speak(obj):
    obj.talk()
d=Duck()
p=Person()
speak(d)
speak(p)