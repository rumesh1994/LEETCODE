class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue)!=0:
            return self.queue.pop(-1)
        else:
            return None
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue)!=0:
            return self.queue[-1]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop() : returns last inserted element
# param_3 = obj.top() : returns last inserted element
# param_4 = obj.empty() : checks if DS is empty

# Stack operations are LIFO while Queue operations are FIFO. While doing the list implementations of stacks and queues,
# keep in mind the default behaviour of a list. 

# l = []
# l.append(1)
# l.append(2)
# l = [1,2]; The first inserted is in index 0 and second inserted is in index 1;