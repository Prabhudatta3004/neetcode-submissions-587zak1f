class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() ## sorts it according to start times

        res = [intervals[0]] ## we will use the last entries end time 

        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res
