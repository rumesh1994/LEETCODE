class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        """
        if n > 0:
            s = int(str(n)[::-1])
        else:
            s = int(str(n)[::-1][-1] + str(n)[::-1][:-1])
        
        #32 bit signed int range as reversed number should fall in this range
        if s <= 2147483647 and s >= -2147483647:
            return s
        else:
            return 0