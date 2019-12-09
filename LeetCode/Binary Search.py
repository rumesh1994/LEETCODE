class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1

# Binary search
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high)//2
#         if target > nums[mid]:
#             low = mid
#         elif target == nums[mid]:
#             break
#         else:
#             high = mid 
#     return mid