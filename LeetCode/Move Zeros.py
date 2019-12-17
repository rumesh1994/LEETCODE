class Solution(object):
    def moveZeroes(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = a.count(0)
        while x>0:
            for i in range(len(a)-1):
                if a[i] == 0:
                    a[i],a[i+1] = a[i+1],a[i]
            x-=1
        return a

# Without any conditions, solution is return [i for i in a if i != 0] + [0]*a.count(0)