class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0

        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd,end)
                count +=1
        return count