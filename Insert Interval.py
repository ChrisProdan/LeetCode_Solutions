class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        Output = []
        newInserted = False

        i = 0
        while (i < len(intervals)):
            if not newInserted:
                if newInterval[0] < intervals[i][0]:
                    Output.append(newInterval)
                    i -= 1
                    newInserted = True
                elif intervals[i][1] >= newInterval[0]:
                    Output.append(intervals[i])
                    Output[-1][1] = max(intervals[i][1],newInterval[1])
                    newInserted = True
                else:
                    Output.append(intervals[i])
            else:
                if intervals[i][0] <= Output[-1][1]:
                    Output[-1][1] = max(intervals[i][1],Output[-1][1])
                else:
                    Output.append(intervals[i])
            i += 1
        
        if not newInserted:
            Output.append(newInterval)

        return Output
        