from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account interest is 5%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account interest is 3%")

s = SavingsAccount()
c = CurrentAccount()

s.calculate_interest()
c.calculate_interest()