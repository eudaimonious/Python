'''
PROBLEM 1: PAYING THE MINIMUM
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
'''

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

def minpayment(balance, annualInterestRate, monthlyPaymentRate):
  totalPaid = 0
  month = 1
  while month <= 12:
      minPayment = monthlyPaymentRate * balance #Compute the monthly payment, based on the previous month's balance.
      balance -=  minPayment #Update the outstanding balance by removing the payment,
      balance += (annualInterestRate/12.0)*balance #then charging interest on the result.
      print 'Month:',month #Output the month,
      print 'Minimum monthly payment:',round(minPayment,2) #the minimum monthly payment
      print 'Remaining balance:',round(balance,2) #and the remaining balance.
      totalPaid += minPayment #Keep track of the total amount of paid over all the past months so far.
      month += 1
  print 'Total paid:', round(totalPaid,2) #Print out the result statement with the total amount paid
  print 'Remaining balance:', round(balance,2) #and the remaining balance.

'''
PROBLEM 2: PAYING DEBT OFF IN A YEAR
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
'''

fixedPayment1 = 0
searching = True

def adequatePayment(balance,annualInterestRate,fixedPayment):
    '''
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    '''
    month = 1
    while month <= 12:
        balance -=  fixedPayment1 #Update the outstanding balance by removing the payment,
        balance += (annualInterestRate/12.0)*balance #then charging interest on the result.
        month += 1
    if balance <= 0:
        return fixedPayment1
    else:
        return False

while searching == True:
    if adequatePayment(balance,annualInterestRate,fixedPayment1):
        searching = False
        print 'Lowest Payment:',adequatePayment(balance,annualInterestRate,fixedPayment1)
    else:
        fixedPayment1 += 10
        adequatePayment(balance,annualInterestRate,fixedPayment1)

'''
PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
'''

monthlyInterestRate = annualInterestRate/12.0
high = (balance * (1 + monthlyInterestRate)**12)/12.0
low = balance/12
fixedPayment2 = (high + low)/2
searching = True

def adequatePayment(balance,monthlyInterestRate,fixedPayment2):
    '''
    balance - the outstanding balance on the credit card
    monthlyInterestRate -  monthly interest rate as a decimal
    '''
    month = 1
    while month <= 12:
        balance -=  fixedPayment2 #Update the outstanding balance by removing the payment,
        balance += monthlyInterestRate*balance #then charging interest on the result.
        month += 1
    return balance

while searching:
    z = adequatePayment(balance,monthlyInterestRate,fixedPayment2)
    if  round(z) < 0:
        high = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) > 0:
        low = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) == 0:
        searching = False
        print 'Lowest Payment:',round(fixedPayment2,2)
