class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * n
        dp[-1] = stoneValue[-1]

        pileSum = [0] * n
        pileSum[-1] = stoneValue[-1]
        for i in range(2,n+1):
            pileSum[-i] = pileSum[-i+1]+stoneValue[-i]

        pileSum.append(0)
        pileSum.append(0)
        dp.append(0)
        dp.append(0)


        for i in range(4,n+3):
            bestMin = min(dp[-i+1:-i+min(4,i-1)])


            dp[-i] = (pileSum[-i] - bestMin) 
        
        if dp[0] > pileSum[0] / 2:
            return "Alice"
        elif dp[0] == pileSum[0] / 2:
            return "Tie"
        else:
            return "Bob"


        