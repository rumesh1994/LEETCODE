import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #Create a counter that has a count of Up: U, down: D, left: L and right:R in moves; The number of up and
        #down should equal down and left counts should equal right counts to get the robot to original position
        count = collections.Counter(moves)
        return count['U'] == count['D'] and count['L'] == count['R']

#Alternate Solution
    #Dedicate a key to Up: U, down: D, left: L and right:R in moves; The sum of these numbers should result in 0 when
    #robot returns to origin
        # directs = {'L':-1, 'R':1, 'U':1j, 'D':-1j}
        # return 0 == sum(directs[move] for move in moves)