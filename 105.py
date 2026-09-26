f = open("transactions.txt", "w")

f.write("Deposit: 5000\n")
f.write("Withdraw: 1000\n")
f.write("Deposit: 2000\n")

f.close()

print("Transactions saved")