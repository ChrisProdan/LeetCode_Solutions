class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = nums[0]
        currentSum = 0
        count = 0
        while True:
            if count + 1 > len(nums):
                break
            
            currentSum += nums[count]
            largestSum = currentSum if currentSum > largestSum else largestSum
            currentSum = 0 if currentSum < 0 else currentSum

            count += 1
        
        return largestSum
            
        