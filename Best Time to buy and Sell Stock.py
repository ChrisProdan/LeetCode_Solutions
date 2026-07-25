class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxProfit = 0
        for x in prices[1:]:
            minSoFar = x if x < minSoFar else minSoFar
            maxProfit = x - minSoFar if x - minSoFar > maxProfit else maxProfit
        
        return maxProfit

        