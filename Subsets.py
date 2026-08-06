class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        Output = [[]]
        for x in nums:
            Output += [subset + [x] for subset in Output]
        
        return Output
        