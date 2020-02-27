def isPalindrome(x):
    reversed = 0
    if x > 0:
        reversed = int(str(x)[::-1])
    if x < 0:
        reversed = int(str(x*-1)[::-1])

    if x == reversed:
        print(x, True)
        return True
    else:
        print(x, False)
        return False

isPalindrome(121)
isPalindrome(-121)
isPalindrome(10)