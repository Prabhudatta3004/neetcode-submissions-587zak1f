class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        curr_sum = 0
        starting_point = 0

        for i in range(len(gas)):
            curr_sum += gas[i]-cost[i]

            if curr_sum<0:
                curr_sum = 0
                starting_point = i+1
        return starting_point