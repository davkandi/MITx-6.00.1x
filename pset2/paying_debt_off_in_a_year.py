payment = 0
initbalance = balance

while (balance > 0):
    payment += 10
    for month in range(1, 13):
        unpaidbalance = balance - payment
        balance = unpaidbalance + (annualInterestRate / 12.0) * unpaidbalance
    if (balance > 0):
        balance = initbalance
    else:
        break
           
print('lowest payment : ' + str(payment))
