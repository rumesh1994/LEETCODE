# Brute Force
s = 'abbac'
y = []
# Check if a string is a palindrome 
isPalindrome = lambda s: s == s[::-1]

# Checks if given string itself is a palindrome
if isPalindrome(s) == True:
    print(True)
else:
    for i in range(0,len(s)):
        # Removes one letter from given string from strat to end and checks if it is a palindrome
        x = s[0:i]+s[i+1:len(s)]
        y.append(isPalindrome(x))
    print(any(y))

# Faster Solution
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = 'abbac'
        # Check if a string is a palindrome
        isPalindrome = lambda s: s == s[::-1]

        # Removes one letter from the given string
        strPart = lambda s, x: s[:x] + s[x + 1:]

        # 2 pointers going both diections
        low = 0
        high = len(s) - 1
        while low < high:
            # Checks if the letters are not same in low and high indices
            if s[low] != s[high]:
                # If the letters are not same, checks if the string is plaindrome by removing letters 
                # from high and low position
                # Iter1: low = 0, high = 4, strPart(s, low) = 'bbac', strPart(s, high) = 'abba'
                return isPalindrome(strPart(s, low)) or isPalindrome(strPart(s, high))
            low += 1
            high -= 1
        return True
