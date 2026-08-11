class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light = 0
        heavy = len(people)-1
        boat_count = 0
        while light <= heavy:
            boat_count +=1
            diff = limit - people[heavy]
            if people[light] <= diff:
                light +=1
            heavy -=1
        return boat_count
