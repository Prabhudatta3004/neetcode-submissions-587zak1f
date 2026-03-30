class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []

        #phase: 1 adding all the intervals that lie before the new interval
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i +=1
        
        ## phase2: adding all the overlapping intervals and creating one big newInterval

        while i<n and intervals[i][0]<= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i +=1
        
        res.append(newInterval)

        ## phase3: adding all the rest of the intervals after the new interval
        while i<n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i +=1
        
        return res