def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base,exp/2)
    elif exp % 2 != 0:
        return base * recurPowerNew(base, exp-1)

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code
    if a <= b:
        smallerInteger = a
    else:
        smallerInteger = b
    for i in range(smallerInteger,0,-1):
        if i == 1:
            return 1
        elif a % i == 0 and b % i == 0:
            return i

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    count = 0
    for i in aStr:
        count += 1
    return count

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == "":
        return 0
    return 1+lenRecur(aStr[0:-1])

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

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if str1 == "" and str2 == "":
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:-1],str2[1:-1])




