import string

print "Hello World!"

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char in 'aAeEiIoOuU'


#Create a new string that is the reverse of a given string
def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    index = -1
    reverse_s = ""
    while abs(index) <= len(s):
        letter = s[index]
        reverse_s += letter
        index -= 1
    return reverse_s

#Create a new string that is a mirror of a given string
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    reverse_s = reverse(s)
    mirror_s = s + reverse_s
    return mirror_s

#Create a new string with all instances of a given letter removed from a given string
def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    missing_letter = ""
    for i in strng:
        if i != letter:
            missing_letter = missing_letter + i
    return missing_letter

#Check if a string is a palindrome
def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    index = -1
    reverse_s = ""
    while abs(index) <= len(s):
        letter = s[index]
        reverse_s += letter
        index -= 1
    return reverse_s == s

#Count number of instances of a substring in a string
def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    count = 0
    index = 0
    compare_s_sub = ""
    while index < len(s):
        if s[index:index+len(sub)] == sub:
            count += 1
            index += 1
        index += 1
    return count

#Create a new string with the first instance of a given substring removed from a given string
def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    i = 0
    while i != -1:
        i = string.find(sub, s)    #i is the index of the first substring's first chracter in the string
        s_start = s[:i]
        s_finish = s[i+len(sub):]
    return s_start + s_finish

#Modify so that sOuack and Quack are spelled correctly
#Used indices and string module for extra credit
"""
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print letter + suffix
"""
import string
def ducks():
    prefixes = "JKLMNOuPQu"
    suffix = "ack"
    index = 0
    while index < len(prefixes)-1:
        if prefixes[index+1] in string.lowercase:
            prefix = prefixes[index:index+2]
            print prefix + suffix
            index += 1
        elif prefixes[index] in string.lowercase:
            index += 1
        else:
            prefix = prefixes[index]
            print prefix + suffix
            index +=1

#Encapsulate in a function and generalize so that it accepts the string and the letter as arguments.
"""
fruit = "banana"
count = 0
for char in fruit:
    if char == 'a':
        count += 1
print count
"""

def count_letters(fruit, letter):
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    print count


#Rewrite above function so that instead of traversing the string, it repeatedly calls find
#with the optional third parameter to locate new occurences of the letter being counted.
def find(strng, ch, start=0):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
"""
def count_letters(fruit, letter):
    count = 0
    index = 0
    while index < len(fruit):
        find(fruit, letter)
        if index >= 0:
            count += 1
            print count
            return count
    return count
    print count
"""
def count_letters(fruit, letter):
    """
    >>> count_letters("Margaret","a")
    2
    >>> count_letters("I am God.","a")
    1
    >>> count_letters("Margaret is a goddess","x")
    0
    """
    count = 0
    index = 0
    while True:
        index = find(fruit, letter, index)
        if index == -1:
            return count
        count += 1
        index += 1

def function_a():
    print "function a was called..."
def function_b():
    print "function b was called..."
def function_c():
    print "function c was called..."

def dispatch(choice):
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print "Invalid choice."

choice=raw_input("Enter a, b or c. ")
dispatch(choice)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
