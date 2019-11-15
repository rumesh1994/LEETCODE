class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # if(v%3 == 0 and v%5 == 0) *** elif(v%3 == 0) *** elif(v%5 == 0) *** else ***
        return ['FizzBuzz' if (v%3 == 0 and v%5 == 0) else 
        'Fizz' if v%3 == 0 else
        'Buzz' if v%5 == 0 else str(v) for v in range(1,n+1)]