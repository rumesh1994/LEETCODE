class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionaries have key-value pairs, unique keys which are unordered and mutable.
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]=d[i]+1
        for key in d:
            if d[key]==1:
                return key