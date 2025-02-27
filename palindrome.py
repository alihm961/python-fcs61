def isPalindrome(word):
    
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    return False

print(isPalindrome("maddam"))


def findMissing(list):
    if len(list) <= 1:
        return None
    
    if list[1] - list[0] != 1:
        return list[0] + 1

    return findMissing(list[1:])

print(findMissing([1, 2, 3, 5, 6]))
