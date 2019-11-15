class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Set contains unique items
        s = set()
        while n != 1:
            #if it is a happy number, the number will not repeat and sum of squares of digit don't add upto 1
            if n in s: return False
            #Add n to set
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            #if it is a happy number, each digit in the number will square and add upto 1
            return True