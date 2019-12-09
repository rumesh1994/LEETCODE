class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l=[a,b]
        return sum(l)

#Alternate way for 2 positive integers a,b
# while b > 0:
#     a+=1
#     b-=1