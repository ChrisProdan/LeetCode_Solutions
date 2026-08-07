class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Output = []
        def combinationBuilder(idx,sum,combinations):
            #return sequence
            if sum == target:
                Output.append(combinations)
                return
            elif sum > target:
                return
            
            if idx == len(candidates)-1:
                newCombinations = combinations.copy()
                newCombinations.append(candidates[idx])
                combinationBuilder(idx,sum+candidates[idx],newCombinations)
            else:
                combinationBuilder(idx+1,sum,combinations)

                newCombinations = combinations.copy()
                newCombinations.append(candidates[idx])
                combinationBuilder(idx,sum+candidates[idx],newCombinations)
        
        combinationBuilder(0,0,[])
        return Output

            


        