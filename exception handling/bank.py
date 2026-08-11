bal:5000
try:
    amount=float(input("enter withdraw amount"))
    if amount<=0:
        raise ValueError("withdraw amount must be greater than zero")
    if amount>bal:
        raise ValueError("insufficrent balance")
    bal=bal-amount
except ValueError as error:
    print("transaction failed:",error)
    