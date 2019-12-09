class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #str.find(sub[, start[, end]]); left to right and returns first occurence else -1 
        return haystack.find(needle)