class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        Output = []
        Output.append(intervals[0])
        for x in intervals[1:]:
            if x[0] <= Output[-1][1]:
                if x[1] > Output[-1][1]:
                    Output[-1][1] = x[1]
                else:
                    continue
            else:
                Output.append(x)
        return Output



        
        