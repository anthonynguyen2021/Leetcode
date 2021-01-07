# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n) where n is the number of nodes in the tree
    # Space = O(d) where d is the height of the tree
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helperBST(root, float('-inf'), float('inf'))
    
    def helperBST(self, node, lower, upper):
        if not node:
            return True
        if not (lower < node.val < upper):
            return False
        else:
            return self.helperBST(node.left, lower, node.val) and self.helperBST(node.right, node.val, upper)
