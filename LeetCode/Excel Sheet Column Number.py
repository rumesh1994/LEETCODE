import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #Convert it to a list
        c = [i for i in s.lower()]
        #reverse the list
        rev = c[::-1]
        # return column number
        col_num = 0
        #created dictionary for values a-z
        d = dict(zip(string.ascii_lowercase, range(1,27)))
        for i in range(0,len(rev)):
            col_num+= d[rev[i]]*pow(26,i)
        return col_num