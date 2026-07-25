class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myDequeue = []
        Output = []

        # Building the sliding window

        for i in range(k):
            while len(myDequeue) > 0 and nums[i] > nums[myDequeue[-1]]:
                myDequeue.pop(-1)           
            myDequeue.append(i)
        
        Output.append(nums[myDequeue[0]])

        # Sliding the Window

        for i in range(k,len(nums)):
            while len(myDequeue) > 0 and nums[i] > nums[myDequeue[-1]]:
                myDequeue.pop(-1)           
            myDequeue.append(i)

            while myDequeue[0] <= i - k:
                myDequeue.pop(0)
            
            Output.append(nums[myDequeue[0]])
        
        return Output

        