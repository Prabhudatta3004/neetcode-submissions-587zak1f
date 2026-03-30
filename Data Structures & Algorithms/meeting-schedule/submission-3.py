class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        # Sort by start time (standard for overlap detection)
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            # If current starts before previous ends, it's a conflict
            if intervals[i].start < intervals[i-1].end:
                return False # Exit early! No need to check the rest
        
        return True # If we made it through, all good