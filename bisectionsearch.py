#secret number

low1 = 0
high1 = 100
lastGuessWas = ''

print 'Please think of a number between 0 and 100!'

while lastGuessWas != 'c':
    guess = (high+low1)/2
    print "Is your secret number " + str(guess) + "?"
    lastGuessWas = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if lastGuessWas != 'l' and lastGuessWas != 'h' and lastGuessWas != 'c':
        print 'Sorry, I did not understand your input.'
    elif lastGuessWas == 'l':
        low1 = guess
    elif lastGuessWas == 'h':
        high1 = guess
    elif lastGuessWas == 'c':
        print "Game over. Your secret number was: " + str(guess)

#minimum to pay off debt in 1 year

monthlyInterestRate = annualInterestRate/12.0
high2 = (balance * (1 + monthlyInterestRate)**12)/12.0
low2 = balance/12
fixedPayment = (high2 + low2)/2
searching = True

def adequatePayment(balance,monthlyInterestRate,fixedPayment):
    '''
    balance - the outstanding balance on the credit card
    monthlyInterestRate -  monthly interest rate as a decimal
    '''
    month = 1
    while month <= 12:
        balance -=  fixedPayment #Update the outstanding balance by removing the payment,
        balance += monthlyInterestRate*balance #then charging interest on the result.
        month += 1
    return balance

while searching:
    z = adequatePayment(balance,monthlyInterestRate,fixedPayment)
    if  round(z) < 0:
        high2 = fixedPayment
        fixedPayment = (high2 + low2)/2
    elif round(z) > 0:
        low2 = fixedPayment
        fixedPayment = (high2 + low2)/2
    elif round(z) == 0:
        searching = False
        print 'Lowest Payment:',round(fixedPayment,2)

#check if a character is in a string with recursion

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr)-1
    middle = (high + low)/2
    if aStr == "" :
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[middle] == char:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle-1])
    else:
        return isIn(char, aStr[middle+1:])



