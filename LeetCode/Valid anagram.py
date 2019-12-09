class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    #Solution 1
        #Anangrams have same letters but form different words
        s1 = [i for i in s]
        s2 = [i for i in t]
        return True if ''.join(sorted(s1)) == ''.join(sorted(s2)) else False

    #Solution 2
        #return True if ''.join(sorted([i for i in s])) == ''.join(sorted([i for i in t])) else False

#Runtime was 48ms, memory used was 14MB for solution 1 while 68ms and 13.5MB if written as solution 2