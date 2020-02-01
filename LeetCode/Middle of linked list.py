# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Set the pointer 
        curr = head

        # Calculate the length of the linked list
        length = 0
        while(curr):
            length+=1
            curr = curr.next

        # Calculate the mid value
        mid = length//2

        # Set the pointer
        curr = head

        # Iterate linked list till mid value and return the last element in it
        for i in range(mid):
            curr = curr.next
        return curr