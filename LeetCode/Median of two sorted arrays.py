class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst=nums1+nums2 #combine both lists
        lst.sort() #sorts the combined list
        median=0
        if len(lst)%2==1:
            #Odd number of items in list has mid value as median
            median = lst[(len(lst)/2)]
        else:
            #Even number of items in list has 2 mid value and average of these two is their median
            median = (float(lst[len(lst)/2]+lst[(len(lst)/2)-1])/2)
        return median