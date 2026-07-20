class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        largestTotalSum = 0

        largestCurrentSum = 1
        largestOddSum = 1
        IncludeOdd = False

        for i in range(len(nums)):

            if nums[i] == 0:
                largestCurrentSum = 1
                largestOddSum = 1
                IncludeOdd = False
                continue

            largestCurrentSum *= nums[i]

            if IncludeOdd:
                largestOddSum *= nums[i]

            
            largestTotalSum = largestCurrentSum if largestCurrentSum > largestTotalSum else largestTotalSum
            largestTotalSum = largestOddSum if IncludeOdd and largestOddSum > largestTotalSum else largestTotalSum

            if nums[i] < 0:
                if not IncludeOdd:
                    IncludeOdd = True
            
        return largestTotalSum


        