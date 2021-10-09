balance = 1467.61
annualInterestRate = 0.599

lower = balance / 12
upper = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0
payment = (lower + upper) / 2
initbalance = balance

while abs(balance) >= 0.01:
    balance = initbalance
    payment = (lower + upper) / 2
    for month in range(1, 13):
        unpaidbalance = balance - payment
        balance = unpaidbalance + (annualInterestRate / 12.0) * unpaidbalance

    if (balance <= 0.01):
        upper = payment
    elif (balance >= 0.01):
        lower = payment
    else:
        break
    payment = (lower + upper) / 2

print('lowest payment:', round(payment, 2))