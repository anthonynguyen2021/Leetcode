# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n)
    # Space = O(h) where h is the height of the tree
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self, root) -> (bool, int):
        if not root:
            return True, -1
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        # Need to check if the left subtree is balanced or not.
        # If this is omitted, we may miss some test case when constructed balanced for root.
        if not leftIsBalanced:
            return False, -1
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, -1
        return abs(leftHeight - rightHeight) < 2, 1 + max(leftHeight, rightHeight)
