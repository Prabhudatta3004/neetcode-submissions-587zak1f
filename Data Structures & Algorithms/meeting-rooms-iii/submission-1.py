import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1. Sort meetings by start time. If start times are equal, 
        # the problem implies we process them in the order given.
        meetings.sort()

        # available: contains room indices [0, 1, 2, ... n-1]
        available = [i for i in range(n)]
        heapq.heapify(available)

        # busy: contains [end_time, room_index]
        busy = []
        
        # To track how many meetings each room hosted
        room_usage_count = [0] * n

        for start, end in meetings:
            # 2. Free up rooms: Move all rooms that finish by 'start' 
            # from 'busy' to 'available'.
            while busy and busy[0][0] <= start:
                _, room_idx = heapq.heappop(busy)
                heapq.heappush(available, room_idx)

            # 3. Assign a room
            if available:
                # Case A: A room is free. Pick the one with the smallest index.
                room_idx = heapq.heappop(available)
                heapq.heappush(busy, [end, room_idx])
            else:
                # Case B: All rooms are busy. Wait for the one ending earliest.
                earliest_end_time, room_idx = heapq.heappop(busy)
                
                # The meeting is delayed. New end time = room's free time + duration.
                duration = end - start
                new_end_time = earliest_end_time + duration
                
                heapq.heappush(busy, [new_end_time, room_idx])

            room_usage_count[room_idx] += 1

        # 4. Return the index of the most used room. 
        # .index(max()) naturally returns the smallest index in case of a tie.
        return room_usage_count.index(max(room_usage_count))