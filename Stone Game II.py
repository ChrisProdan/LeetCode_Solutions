class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)

        pileSum = [0] * n
        pileSum[-1] = piles[-1]

        for i in range(2,n+1):
            pileSum[-i] = pileSum[-i + 1]+piles[-i]
        
        dp = [[0] * n for _ in range(n - 1)]
        dp.append([pileSum[-1]]*n)

        for i in range(2,n+1):
            for j in range(n):
                M = j+1
                pilesLeft = i

                if 2*(M) >= (pilesLeft):
                    dp[-i][j] = pileSum[-i]
                else:
                    minNext = 100000000000
                    for k in range(1,(2*M)+1):
                        if dp[-i + k][max(M,k)-1] < minNext:
                            minNext = dp[-i + k][max(M,k)-1]

                    dp[-i][j] = pileSum[-i] - minNext
        
        return dp[0][0]

                
        

        
        