class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # dictionary key is letter and its value is count of the letter; check count by taking minimum
        # of count of letters that form balloon.
        dict = {}
        for i in 'balloon':
            dict[i] = text.count(i)
        return min(dict['b'],dict['a'],dict['l']/2,dict['o']/2,dict['n'])