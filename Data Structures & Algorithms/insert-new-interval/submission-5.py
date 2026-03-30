class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res= []

        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i +=1
        
        while i<n and intervals[i][0] <= newInterval[1]:
            minstart = min(intervals[i][0],newInterval[0])
            maxend = max(intervals[i][1],newInterval[1])
            newInterval = [minstart,maxend]
            i +=1
        res.append(newInterval)

        while i<n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i +=1
        return res