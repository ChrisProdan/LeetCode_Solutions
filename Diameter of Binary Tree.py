# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            else:
                return 1 + max(maxDepth(root.left),maxDepth(root.right))

        if root == None:
            return 0
        return max(maxDepth(root.left) + maxDepth(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        