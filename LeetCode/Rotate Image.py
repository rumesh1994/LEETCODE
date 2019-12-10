class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # First transpose the matrix A
        # A = [[1,2,3],[4,5,6],[7,8,9]]
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
                # A = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        # Next reverse the matrix A to get 90deg rotation
        for i in range(len(A)):
            A[i].reverse()
        # Output: A = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        return A