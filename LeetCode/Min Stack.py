class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.stack)==1:
            self.min = x
        else: 
            for i in self.stack:
                if i <= self.min:
                    self.min = i
        
    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)>1:
            a = self.stack.pop()
            print(a)
            if a == self.min:
                self.min = self.stack[0]
                for i in self.stack:
                    if i <=self.min:
                        self.min = i
        elif len(self.stack) == 1:
            self.min = None
            self.stack.pop()
        else:
            pass

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.min
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()