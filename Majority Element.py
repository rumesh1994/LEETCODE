class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # element that appears more than ⌊ n/2 ⌋ times
        return sorted(nums)[len(nums)/2]