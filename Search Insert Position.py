class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if(nums[-1] < target):
            return len(nums)
        elif(nums[0] > target):
            return 0

        while(high >= low):
            med = low + (high - low) // 2

            if(nums[med] == target):
                return med
            elif(nums[med] < target and nums[med+1] > target):
                return med+1
            elif(nums[med] > target):
                high = med-1
            else:
                low = med+1
        
        return -1

        