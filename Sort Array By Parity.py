class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #sorted(iterable, *, key=None, reverse=False)
        return sorted(A, key = lambda x : x % 2)