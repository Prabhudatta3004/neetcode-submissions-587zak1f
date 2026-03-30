class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ## [2,3] , [4,5], [6,7]
        
        ## [12,1]3,4 ## 

        ## [2,5]
        res = []
        for i in range(len(intervals)):
            ## newinterval[1] < interval[i][0]
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            ## newInterval[0] > interval[i][1]

            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res