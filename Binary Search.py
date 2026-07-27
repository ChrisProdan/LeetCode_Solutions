class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        mp = (rp + lp) // 2 
        
        while lp < rp:
            if nums[mp] == target:
                return mp
            elif nums[mp] > target:
                rp = mp - 1
            else:
                lp = mp + 1
            
            mp = (rp + lp) // 2
        
        if nums[lp] == target:
            return lp
        else:
            return -1


        