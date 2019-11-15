class Solution:
    def searchInsert(self, nums, target) -> int:
        #append number to existing list
        nums.append(target)
        #sort the list and return the index
        return sorted(nums).index(target)