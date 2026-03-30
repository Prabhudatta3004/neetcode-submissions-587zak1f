class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)

        if sum(matchsticks)%4 != 0:
            return False
        
        side_length = sum(matchsticks)//4

        sides = [0] * 4

        def backtrack(stick_id):
            if stick_id == len(matchsticks):
                return True
            
            for side_id in range(4):
                if sides[side_id] + matchsticks[stick_id] <=side_length:
                    sides[side_id] += matchsticks[stick_id]
                    if backtrack(stick_id+1):
                        return True
                    sides[side_id] -= matchsticks[stick_id]
            return False
        return backtrack(0)
