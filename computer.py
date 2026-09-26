class CPU:
    def process(self):
        print("CPU processes")
class Computer:
    def __init__(self):
        self.cpu = CPU()
c = Computer()
c.cpu.process()