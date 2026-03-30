class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events= []
        for num_passengers,start,end in trips:
            events.append((start,num_passengers))
            events.append((end,-num_passengers))

        events.sort()

        curr_passengers = 0
        for location, change in events:
            curr_passengers +=change

            if curr_passengers > capacity:
                return False
        return True