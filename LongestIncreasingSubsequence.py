class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.insert(0,[nums[-1],1])
        currLongest = 1

        for i in range(2,len(nums)+1):
            tempLongest = 0
            for x in dp:
                if x[0] > nums[-i] and x[1] > tempLongest:
                    tempLongest = x[1]
            dp.insert(0,[nums[-i],1+tempLongest])
            currLongest = 1 + tempLongest if 1 + tempLongest > currLongest else currLongest
        
        return currLongest
        


        