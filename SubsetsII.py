class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        newNums = [[nums[0],1]]

        for x in nums[1:]:
            if newNums[-1][0] != x:
                newNums.append([x,1])
            else:
                newNums[-1][1] += 1

        Output = [[]]

        for pair in newNums:
            length = len(Output)

            for i in range(pair[1]):
                for j in range(length):
                    newSet = Output[-length].copy()
                    newSet.append(pair[0])
                    Output.append(newSet)
        
        return Output


        