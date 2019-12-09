class Solution(object):
    def isPalindrome(self, n):
        """
        :type x: int
        :rtype: bool
        """
        if n >= 0:
            if str(n)[::-1] == str(n):
                return True
            else:
                return False
        else:
            return False