class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strsSorted = []

        for s in strs:
            strsSorted.append("".join(sorted(s)))
        
        Output = [[strs[0]]]
        Storage = dict()

        Storage.update({strsSorted[0]:0})

        count = 1
        countBuckets = 1
        for s in strsSorted[1:]:
            if s not in Storage:
                Storage.update({strsSorted[count]:countBuckets})
                Output.append([strs[count]])
                countBuckets += 1
                count += 1
            else:
                Output[Storage[s]].append(strs[count])
                count += 1
        
        return Output
            
        