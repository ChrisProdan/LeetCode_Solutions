# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inBST(rootTemp, n):
            if rootTemp == None:
                return False
            elif rootTemp.val == n:
                return True
            elif n > rootTemp.val:
                return inBST(rootTemp.right,n)
            else:
                return inBST(rootTemp.left,n)
        
        pInLeft = inBST(root.left,p.val)
        pInRight = inBST(root.right,p.val)
        qInLeft = inBST(root.left,q.val)
        qInRight = inBST(root.right,q.val)

        if p.val == root.val or q.val == root.val:
            return root


        if (pInLeft and qInRight) or (pInRight and qInLeft):
            return root
        elif pInLeft:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)

        
            

        