class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## the interval can be inserted before all the intervals
        ## An already existing interval that finishes before
        ## the new interval can be inserted
        ## then I can consider to add the interval in between and
        ## get the min of start points and max of end points to
        ## make one interval based on overlapping

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),
                max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res
