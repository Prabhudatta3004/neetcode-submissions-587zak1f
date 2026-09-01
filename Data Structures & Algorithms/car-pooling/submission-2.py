class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for num_passengers,start,end in trips:
            events.append([start,num_passengers])
            events.append([end,-num_passengers])
        events.sort()
        
        curr_capacity = 0
        for _,num_passengers in events:
            curr_capacity += num_passengers

            if curr_capacity > capacity:
                return False
        return True