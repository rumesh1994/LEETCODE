"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        l = []
        
        if root.children:
            for node in root.children:
                l.extend(self.postorder(node))
                
        return l + [root.val]