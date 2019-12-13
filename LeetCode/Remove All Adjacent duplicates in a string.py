class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        lstack = []
        for c in S:
            # if adjacent value is the same, pops the value from lstack
            if lstack and c == lstack[-1]:
                lstack.pop()
                continue
            # char c is appended that appears first time and is retained if adjacent value is not the same
            lstack.append(c)
        return ''.join(lstack)