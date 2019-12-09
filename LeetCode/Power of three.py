class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n%3 == 0:
                n /= 3
            else:
                #n has any other factors apart from 3
                return False
        if n == 1:
            #n is 1 only if it is only divisible by 3
            return True
        else: 
            # n <= 0
            return False