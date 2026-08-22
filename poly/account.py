class BankAccount:
    def withdraw(self):
        print("Withdraw from Bank Account")
class SavingsAccount(BankAccount):
    def withdraw(self):
        print("Withdraw from Savings Account")
account=SavingsAccount()
account.withdraw()