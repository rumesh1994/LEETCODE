# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary = 0
        
        # Run until the null pointer is reached in the linked list
        while head is not None:
            binary *= 2
            binary += head.val
            head = head.next
        return binary

