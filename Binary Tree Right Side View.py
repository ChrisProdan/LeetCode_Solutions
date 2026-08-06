# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        Output = []
        def levelOrderHelper(rootTemp,level):
            if rootTemp == None:
                return
            if len(Output) <= level:
                Output.append([])
            Output[level].append(rootTemp.val)
            levelOrderHelper(rootTemp.left,level + 1)
            levelOrderHelper(rootTemp.right,level + 1)

        levelOrderHelper(root,0)
        Output = list(map(lambda x: x[-1],Output))
        return Output