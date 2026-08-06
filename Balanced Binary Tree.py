# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            else:
                return 1 + max(maxDepth(root.left),maxDepth(root.right))

        if root == None:
            return True
        elif abs(maxDepth(root.left) - maxDepth(root.right)) >= 2:
            return False            
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        