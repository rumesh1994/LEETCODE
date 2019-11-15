class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Keeps a track of opening brackets in s (stack implemented as a list)
        pars = []
        #Hash map of pairs of parentheses
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if(c in ["(", "{", "["]):
                #We have an opening bracket, simply push it onto the stack
                pars.append(c)
            elif len(pars) == 0 or parmap[c] != pars.pop():
                #Element of the stack don't match, return False
                return False
        #We have a valid expression if the stack is empty
        return len(pars) == 0
        