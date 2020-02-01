# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initially set previous node pointer to null
        prev = None

        # Until end of linked list
        while head:
            # temp variable to store current node
            temp = head

            # point current node to next node
            head = head.next

            # point current node to the previous node
            temp.next = prev
            prev = temp
        return prev