class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Storage = dict()
        for x in nums:
            if x in Storage:
                return True
            else:
                Storage.update({x : "Here"})
        
        return False

        