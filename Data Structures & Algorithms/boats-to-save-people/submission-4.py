class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        thin = 0
        thick = len(people)-1

        boats = 0

        while thin <= thick:
            remainder = limit - people[thick]
            if remainder > 0 and people[thin] <= remainder:
                thin +=1
            boats +=1
            thick -=1
        return boats