class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negNumbers = 0
        for row in grid:
            for col in row:
                if col < 0:
                    negNumbers += 1
        return negNumbers