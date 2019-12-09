class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #inner loop reverse and return compliment and out loop iterates over rows
        return [[1-val for val in row[::-1]] for row in A]

    #Alternate way
    # flipped = []
    #     for row in A:
    #Reverse the row and then take inverse
    #         flipped.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
    #     return flipped