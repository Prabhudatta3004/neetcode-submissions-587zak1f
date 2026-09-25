class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        curr_sum = 0
        starting_point = 0

        for idx in range(len(gas)):
            curr_sum += gas[idx]-cost[idx]
            if curr_sum<0:
                curr_sum = 0
                starting_point = idx+1
        return starting_point