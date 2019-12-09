class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Return length of last word unless it is not a null string
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0