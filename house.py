class Room:
    def show(self):
        print("Room")
class House:
    def __init__(self):
        self.room = Room()
h = House()
h.room.show()