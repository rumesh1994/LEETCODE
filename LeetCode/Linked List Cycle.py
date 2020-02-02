# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Keys are the locations ids of elements in linked list to be stored in a dictionary
        dict = {} 
        while head:
            # If id exists, it has a cycle and else add it in the dictionary
            if id(head) in dict:
                return True
            else:
                dict[id(head)] = True
            head = head.next
        return False

# Other Solution
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         prev = nxt = head
#         while nxt and nxt.next:
#             prev = prev.next
#             nxt = nxt.next.next
#             if prev == nxt:
#                 return True
#         return False

        