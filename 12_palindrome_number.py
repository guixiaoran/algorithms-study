def isPalindrome(x) -> bool:
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[-i-1]:
            return False


    return True

print(isPalindrome(121))