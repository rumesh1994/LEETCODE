class Solution(object):
    def detectCapitalUse(self, s):
        """
        :type word: str
        :rtype: bool
        """
        #Check if lower case, UPPER CASE or Title
        return s.istitle() or s.isupper() or s.islower()