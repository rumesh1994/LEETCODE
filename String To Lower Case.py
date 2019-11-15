class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

# class Solution(object):
#     def toLowerCase(self, str):
#         """
#         :type str: str
#         :rtype: str
#         """
#         #ord('a')=97 and ord('A')=65, calculate this difference; To convert B to b, ord('b')= ord('B') + gap
#         gap = ord('a') - ord('A')
#         return ''.join([chr(ord(c) + gap) if ord(c) >= ord('A') and ord(c) <= ord('Z') else c for c in str])