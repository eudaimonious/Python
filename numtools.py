def compare(x,y):
    if x < y:
        print x,"is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"

def is_divisible_by_n(x,n):
    if x%n == 0:
        print "Yes,", x, "is divisible by",n
    else:
        print "No,", x, "is not divisible by", n

def is_prime(x):
    """
    >>> is_prime(2)
    True
    >>> is_prime(233)
    True
    >>> is_prime(4)
    False
    >>> is_prime(234)
    False
    """
    y=x-1
    while y>1:
        if x%y == 0:
            return False
        y=y-1
    return True

def num_digits(n):
    """
    >>> num_digits(12345)
    5
    >>> num_digits(0)
    1
    >>> num_digits(-12345)
    5
    """
    counter=0
    q=10
    if n == 0:
        return 1
    while n != 0 and n != -1:
        n = n/q
        counter += 1
      #  q = q*10
    return counter

def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    counter = 0
    #done when n=0
    while n != 0:
    #modulo to get last digit,
        digit = n%10
    #modulo to test for parity
        if digit%2 == 0:
            counter += 1
    #division to get rid of last digit
        n = n/10
    return counter

def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
    """
    while n!= 0:
        digit = n%10
        print digit,
        n=n/10

def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    counter = 0
    while n!= 0:
        counter = counter +(n%10)**2
        n = n/10
    return counter


def print_multiples(n, high):
    i = 1
    while i<= high:
        print n * i, '\t',
        i+= 1
    print

def print_mult_table(high):
    i=1
    while i<= high:
        print_multiples(i, i)
        i+= 1

print print_mult_table(7)

def compare(a, b):
    """
        >>> compare(5, 4)
        1
        >>> compare(7, 7)
        0
        >>> compare(2, 3)
        -1
        >>> compare(42, 1)
        1
    """
    if a>b:
        return 1
    if a == b:
        return 0
    if a<b:
        return -1

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(lo,x),hi)


def distance(xc, yc, xp, yp):
    dx = xc-xp
    dy = yc-yp
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result
def area(radius):
    return 3.14159 * radius**2
def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def hypotenuse(a,b):
    """
        >>> hypotenuse(3, 4)
        5.0
        >>> hypotenuse(12, 5)
        13.0
        >>> hypotenuse(7, 24)
        25.0
        >>> hypotenuse(9, 12)
        15.0
    """
    return (a**2 + b**2)**0.5


def slope(x1, y1, x2, y2):
    """
        >>> slope(5, 3, 4, 2)
        1.0
        >>> slope(1, 2, 3, 2)
        0.0
        >>> slope(1, 2, 3, 3)
        0.5
        >>> slope(2, 4, 1, 2)
        2.0
    """
    return float(y2 - y1)/float(x2-x1)


def intercept(x1, y1, x2, y2):
    """
        >>> intercept(1, 6, 3, 12)
        3.0
        >>> intercept(6, 1, 1, 6)
        7.0
        >>> intercept(4, 6, 12, 8)
        5.0
    """
    m = slope(x1, y1, x2, y2)
    return y1 - m * x1

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c


def is_even(n):
    """
        >>> is_even(2)
        True
        >>> is_even(1)
        False
        >>> is_even(458)
        True
        >>> is_even(999)
        False
    """
    return n%2 == 0


def is_odd(n):
    """
        >>> is_odd(9)
        True
        >>> is_odd(58)
        False
    """
    if is_even(n):
        return False
    else:
        return True

def print_parity(x):
    if x%2 == 0:
        print x, "is even"
    else:
        print x, "is odd"


def is_factor(f, n):
    """
        >>> is_factor(3,12)
        True
        >>> is_factor(5,12)
        False
        >>> is_factor(7,14)
        True
        >>> is_factor(2,14)
        True
        >>> is_factor(7,15)
        False
    """
    return n%f == 0

def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    if is_factor(n,m):
        return True
    else:
        return False

def f2c(t):
    """
      >>> f2c(212)
      100
      >>> f2c(32)
      0
      >>> f2c(-40)
      -40
      >>> f2c(36)
      2
      >>> f2c(37)
      3
      >>> f2c(38)
      3
      >>> f2c(39)
      4
    """
    c=(5.0/9)*(t-32)
    celsius = round(c)
    return int(celsius)

def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    f=(9.0/5)*t+32
    farenheit = round(f)
    return int(farenheit)

def print_triangular_numbers(n):
    number = 1
    while number <= n:
        print number, '\t', number*(number+1)/2
        number = number + 1

print_triangular_numbers(5)

def print_square_root(x):
    if x <= 0:
        print "Positive numbers only, please."
        return

    result = x**0.5
    print "The square root of", x, "is", result

def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    print better
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
        print better
    return approx

print sqrt(25)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
