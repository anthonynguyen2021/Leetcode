# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    # Time - O(n)
    # Space - O(d) where d is the height of the tree
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helperSym(root.left, root.right)
        
    def helperSym(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and self.helperSym(node1.right, node2.left) and self.helperSym(node1.left, node2.right)
    
