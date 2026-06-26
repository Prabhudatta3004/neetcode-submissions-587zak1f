class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start = 0
        end = len(people)-1
        count=0
        while start<=end:
            remaining= limit - people[end]
            
            if people[start] <= remaining:
                start +=1
            
            count +=1
            end -=1
        return count