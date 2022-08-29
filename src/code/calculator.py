def addition(a, b):
    """ This function adds b to a and returns result. """
    return a + b


def subtraction(a, b):
    """ This function subtracts b from a and returns result. """
    return a - b


def multiplication(a, b):
    """ This function returns a multiply by b. """
    return a * b


def division(a, b):
    """ This function returns a by b. """
    return a / b


def mod(a, b):
    """ This function returns a mod b. """
    return a % b


def power(a, b):
    """ This function returns a power b. """
    return a ** b

def isPalindrome(str):
    # This function checks if the input string is a palindrome or not
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True