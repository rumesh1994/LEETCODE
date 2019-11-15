from collections import Counter 
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #Set has unique items and it is mutable and unordered; If the frequencies of all items in the arr are unique,
        #then the length of set and counter will be same
        return True if len(set(Counter(arr).values())) == len(Counter(arr).values()) else False