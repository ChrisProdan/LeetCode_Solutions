class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        Output = []
        candidates.sort()

        newCandidates = []
        newCandidates.append([candidates[0],1])

        for x in candidates[1:]:
            if newCandidates[-1][0] == x:
                newCandidates[-1][1] += 1
            else:
                newCandidates.append([x,1])
        

        def combinationBuilder(idx,Sum,combinations):
            #return sequence
            if idx >= len(newCandidates):
                if Sum == target:
                    Output.append(combinations)
                    return
                return

            if Sum == target:
                Output.append(combinations)
                return
            elif Sum > target:
                return
            
            for i in range(newCandidates[idx][1] + 1):                
                combinationBuilder(idx+1,Sum,combinations.copy())

                Sum += newCandidates[idx][0]
                combinations.append(newCandidates[idx][0])

        
        combinationBuilder(0,0,[])
        return Output