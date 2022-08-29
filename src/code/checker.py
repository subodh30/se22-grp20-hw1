def isPalindrome(str):
    # This function checks if the input string is a palindrome or not
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True