class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        width = len(grid[0])
        height = len(grid)

        dp = [[[0] * width for _ in range(width)] for __ in range(height)]



        for i in range(height):
            for j in range(width):
                for k in range(width):
                    if i == 0:
                        dp[i][j][k] = grid[-1][j] + grid[-1][k] if j != k else grid[-1][k]
                    else:
                        dp[i][j][k] = grid[-i - 1][j] + grid[-i - 1][k] if j != k else grid[-i - 1][k]
                        
                        dpAdder = 0
                        for j1 in range(max(0,j-1),min(j+2,width)):
                            for k1 in range(max(0,k-1),min(k+2,width)):
                                dpAdder = max(dpAdder,dp[i-1][j1][k1])

                        dp[i][j][k] += dpAdder
        return dp[-1][0][-1]
        