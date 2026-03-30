class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        end = intervals[0][1]
        i = 1
        count = 0
        while i < len(intervals):
            if intervals[i][0] < end:
                count +=1
            else:
                end = intervals[i][1]
            i +=1
        return count