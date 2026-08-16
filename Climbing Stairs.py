class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        oneAgo = 2
        twoAgo = 1
        Ways = 0
        for i in range(n-2):
            Ways = oneAgo + twoAgo
            twoAgo = oneAgo
            oneAgo = Ways
        
        return Ways

        