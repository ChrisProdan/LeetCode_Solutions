class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = "Invalid"
        nums.append("Invalid")

        for i in range(len(nums)):

            if isinstance(nums[i], int) and abs(nums[i]) < len(nums):
                if nums[abs(nums[i])] == "Invalid":
                    nums[abs(nums[i])] = "Seen"
                elif isinstance(nums[abs(nums[i])], int) and nums[abs(nums[i])] > 0:
                    nums[abs(nums[i])] = -nums[abs(nums[i])]
        
        for i in range(1,len(nums)):
            if nums[i] == "Invalid" or (isinstance(nums[i], int) and nums[i] > 0):
                return i
        else:
            return len(nums)