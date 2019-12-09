class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The logic of climbing stairs is fibonacci series. This can be therefore considered as a
        # problem of dynamic programming.
        # This step initialises the list to 1 
        fib = [1 for i in range(n+1)]

        # This function updates the list from 2 till n+1 as fibonacci series and returns the fib[n]
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]

# Example: n = 4, initially fib = [1,1,1,1,1] and after updating fib = [1, 1, 2, 3, 5].