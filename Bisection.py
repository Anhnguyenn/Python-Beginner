# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Problem Set 2, problem 3

# Use bisection search to make the program faster

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Problem Summary: Use bisection search to search for the smallest monthly payment
# to the cent such that we can pay off the entire balance within a year.

# Test Case 1
##balance = 320000
##annualInterestRate = 0.2

##Test Case 2
##balance = 999999
##annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
balance2 = balance
low = balance / 12.0
high = (balance*((1 + monthlyInterestRate)**12)/12.0)
epsilon = 0.00

while round(balance,2) != epsilon:
    lowestPayment = (low + high)/2.0
    balance = balance2
    for i in range (0,12):
        monthlyUnpaidBalance = balance - lowestPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    if round(balance,2) >= 0:
        low = lowestPayment
    else:
        high = lowestPayment
    lowestPayment = (low + high)/2.0
print(round(lowestPayment,2))
