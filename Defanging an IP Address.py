class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return ''.join(['[.]' if i == '.' else i for i in address])