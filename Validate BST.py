# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Output = []
        def flatten(root):
            if root == None:
                return
            
            flatten(root.left)
            Output.append(root.val)
            flatten(root.right)
        
        flatten(root)

        return all(Output[i] < Output[i+1] for i in range(len(Output)-1))

        

        
        