class Solution:
    def jump(self, nums: List[int]) -> int:

        Count = 0
        i = 0
        n = len(nums)
        if n == 1:
            return 0
        
        while True:
            if i + nums[i] >= n-1:
                return Count + 1
            else:
                bestJumpPos = i+1 
                bestJumpDis = i+1 + nums[i+1]
                for j in range(i+1, i + 1 + nums[i]):
                    if j + nums[j] > bestJumpDis:
                        bestJumpPos = j
                        bestJumpDis = j + nums[j]
                
                i = bestJumpPos
                Count += 1

        