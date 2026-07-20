class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        Storage = dict()
        for x in nums:
            if x not in Storage:
                Storage[x] = 0

        longestChain = 1
        currentChain = 1

        for x in nums:
            if x not in Storage:
                continue
            temp = x
            while temp - 1 in Storage:
                temp -= 1
            
            while temp in Storage:
                Storage.pop(temp)
                longestChain = currentChain if currentChain > longestChain else longestChain
                currentChain += 1
                temp += 1
        
            currentChain = 1

        return longestChain

        