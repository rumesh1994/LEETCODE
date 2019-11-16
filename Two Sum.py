class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        #enumerate(iterable, start=0)
        for index, num in enumerate(nums):
            n = target - num
            if n in hmap:
                #if item in map then the pair adds upto the target value
                return [hmap[n], index]
            else:
                hmap[num] = index