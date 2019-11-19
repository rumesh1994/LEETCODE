class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        # Output: [9,4]
        # Perform set intersection
        return list(set(nums1) & set(nums2))