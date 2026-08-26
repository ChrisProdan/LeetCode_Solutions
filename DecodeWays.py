class Solution:
    def numDecodings(self, s: str) -> int:
        dp = []

        for i in range(1,len(s)+1):
            if int(s[-i]) == 0:
                dp.insert(0,0)           
            elif i == 1:
                dp.insert(0,1)
            elif i == 2:
                if int(s[-i]) >= 3 or (int(s[-i]) == 2 and int(s[-i+1]) >= 7):
                    dp.insert(0,dp[0])
                else:
                    dp.insert(0,1 + dp[0])
            else:
                if int(s[-i]) >= 3 or (int(s[-i]) == 2 and int(s[-i+1]) >= 7):
                    dp.insert(0,dp[0])
                else:
                    dp.insert(0,dp[0] + dp[1])
            
        return dp[0]
            
        