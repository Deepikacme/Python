from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Balance: 10000")

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Interest: 500")

obj = SavingsAccount()
obj.calculate_interest()
obj.display_balance()