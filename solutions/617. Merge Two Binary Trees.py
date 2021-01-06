# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # T(n) = O(n)
    # S(n) = O(d) where d is the depth of the tree
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            t3 = None
        elif not t1 or not t2:
            t3 = t1 if t1 else t2
        else:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        return t3
​
