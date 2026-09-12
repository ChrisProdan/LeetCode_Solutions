class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0])] * len(grid)
        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                up = dp[i][j-1] if i == 0 else dp[i-1][j]
                left = dp[i-1][j] if j == 0 else dp[i][j-1]

                dp[i][j] = min(up,left) + grid[i][j]
        
        return dp[-1][-1]
        