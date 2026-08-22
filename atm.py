from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def balance(self):
        pass


class Bank(ATM):
    def __init__(self):
        self.amount = 10000

    def withdraw(self, amount):
        self.amount -= amount
        print("Withdrawn =", amount)

    def deposit(self, amount):
        self.amount += amount
        print("Deposited =", amount)

    def balance(self):
        print("Balance =", self.amount)
bank = Bank()
bank.withdraw(2000)
bank.deposit(3000)
bank.balance()