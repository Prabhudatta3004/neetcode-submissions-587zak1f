class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prevEnd = intervals[0][1]

        res = 0

        for idx in range(1,len(intervals)):
            if intervals[idx][0] < prevEnd:
                res +=1
            else:
                prevEnd = intervals[idx][1]
        return res
