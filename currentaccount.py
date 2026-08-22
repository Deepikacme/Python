from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def display(self):
        pass

class SavingsAccount(Account):
    def display(self):
        print("Savings Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

class CurrentAccount(Account):
    def display(self):
        print("Current Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

s = SavingsAccount(10101, 50000)
c = CurrentAccount(20202, 75000)

s.display()
c.display()