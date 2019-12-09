class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        split, count = 0, 0      
        for c in s:
            count += 1 if c == 'L' else -1 
            #count is zero when L and R are equal and hence split count ++           
            if count == 0:
                split += 1
        return split