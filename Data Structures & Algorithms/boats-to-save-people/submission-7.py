class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0

        people.sort()

        thin = 0
        heavy = len(people)-1

        while thin<=heavy:
            remaining = limit - people[heavy]
            if remaining>0 and people[thin] <= remaining:
                thin +=1
            heavy -=1
            count +=1
        return count