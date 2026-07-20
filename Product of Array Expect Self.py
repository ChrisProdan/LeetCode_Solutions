class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        RighttoLeft = []
        LefttoRight = []

        for i in range(len(nums)):
            if i == 0:
                LefttoRight.append(1)
            else:
                LefttoRight.append(LefttoRight[i-1]*nums[i-1])
        
        for i in range(len(nums)):
            if i == 0:
                RighttoLeft.append(1)
            else:
                RighttoLeft.append(RighttoLeft[i-1]*nums[-(i)])
        
        RighttoLeft.reverse()

        Output = []

        for i in range(len(nums)):
            Output.append(RighttoLeft[i]*LefttoRight[i])
        return Output


        