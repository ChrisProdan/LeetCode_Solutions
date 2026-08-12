class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retval = []

        def permutationBuilder(idx,output):
            if idx == len(nums):
                retval.append(output)
                return
            
            for i in range(len(output)+1):
                newCopy = output.copy()
                newCopy.insert(i,nums[idx])

                permutationBuilder(idx+1,newCopy)
        
        permutationBuilder(0,[])
        return retval


        