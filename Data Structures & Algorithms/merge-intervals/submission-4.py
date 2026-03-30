class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        i = 0

        while i < len(intervals):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1],res[-1][1])
            else:
                res.append(intervals[i])
            i +=1
        return res