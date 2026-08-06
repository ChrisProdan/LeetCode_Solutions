# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root,curMax):
            if root == None:
                return 0
            elif root.val >= curMax:
                return 1 + goodNodesHelper(root.left,root.val) + goodNodesHelper(root.right,root.val)
            else:
                return goodNodesHelper(root.left,curMax) + goodNodesHelper(root.right,curMax)
        
        return goodNodesHelper(root,-100000)
        