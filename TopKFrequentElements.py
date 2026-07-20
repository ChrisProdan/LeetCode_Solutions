class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        Storage = dict()

        for x in nums:
            if x in Storage:
                Storage[x] += 1
            else:
                Storage[x] = 1
        
        Values = Storage.values()
        Elements = Storage.keys()

        sorted_values, sorted_elements = zip(*sorted(zip(Values, Elements)))

        Output = []
        for i in range(k):
            Output.append(sorted_elements[-(i+1)])

        return Output




        