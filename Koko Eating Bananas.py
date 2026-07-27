class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def Valid(k) -> bool:
            count = 0
            for x in piles:
                count += math.ceil(x / k)
            
            return count <= h
        

        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2
            if Valid(mid):
                high = mid
            else:
                low = mid + 1
            
        
        return low
        






        