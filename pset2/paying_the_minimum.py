totalPaid = 0
for month in range(1, 13):
    minpayment = balance * monthlyPaymentRate
    totalPaid = totalPaid + minpayment
    unpaidbalance = balance - minpayment
    balance = unpaidbalance + (annualInterestRate / 12.0) * unpaidbalance
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minpayment, 2)))
    print('Remaining Balance: ' + str(round(balance, 2)))
    
print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining Balance : ' + str(round(balance, 2)))
