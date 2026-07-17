class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash_Map = dict()
        count = 0
        for x in nums:
            if target - x in Hash_Map:
                return [Hash_Map[target-x], count]
            elif x not in Hash_Map:
                Hash_Map.update({x: count})

            count += 1
            