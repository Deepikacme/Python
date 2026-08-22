from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Account Holder:", self.holder)
        print("Account Number:", self.account_number)
        print("Interest: 5%")

s = SavingsAccount("Deepika", 12345)
s.calculate_interest()