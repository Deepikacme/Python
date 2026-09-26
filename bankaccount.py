class BankAccount:
    def account(self):
        print("Bank account")
class SavingsAccount(BankAccount):
    pass
class CurrentAccount(BankAccount):
    pass
SavingsAccount().account()
CurrentAccount().account()