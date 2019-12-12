class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack)!= 0:
            return self.stack.pop(0)
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack)!= 0:
            return self.stack[0]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

# Peek shows first inserted element
# Pop returns first inserted element : pop(0); By default: returns last inserted element
# Always keep a check on length and DS used here is a list implementation