# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Set current pointer on head
        current = head

        while current:
            # Check if the value of element at i and i+1 position are the same
            if current.next and current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head