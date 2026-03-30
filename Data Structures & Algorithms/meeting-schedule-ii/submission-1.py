"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = 0
        e = 0
        starts = sorted([i.start for i in intervals])
        end  = sorted([i.end for i in intervals])
        res = 0
        count = 0
        while s<len(intervals):
            if starts[s] < end[e]:
                count +=1
                s +=1
            else:
                count -=1
                e +=1
            
            res = max(res,count)
        return res