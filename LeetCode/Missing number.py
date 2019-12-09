class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # one missing number in a sequence is deteted by sum of n integers - sum of all numbers in list
        n = len(nums)
        return n*(n+1)/2 - sum(nums)