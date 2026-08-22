from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def account_type(self):
        print("Account Type: Savings Account")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("Account Type: Current Account")


accounts = [
    SavingsAccount("Deepika", 50000),
    CurrentAccount("Rahul", 75000)
]

for account in accounts:
    account.account_type()
    account.display()
    print()