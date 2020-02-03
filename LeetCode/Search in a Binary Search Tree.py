# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # In a BST, the left node to root is lesser than root and right node to root
        # is greater than root.

        if not root:
            return None

        # Traverse left of tree if val < root value 
        if root.val > val:
            return self.searchBST(root.left,val)

        # Traverse right of tree if val > root value 
        if root.val < val:
            return self.searchBST(root.right,val)

        return root