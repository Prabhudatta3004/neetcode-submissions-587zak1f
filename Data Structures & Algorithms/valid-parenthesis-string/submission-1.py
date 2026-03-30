class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            
            ## both low and high increases with open bracket
            if c == "(":
                low +=1
                high +=1
            ## both low and high decreases with a closed bracket
            elif c == ")":
                low -=1
                high -=1
            ## now considering *, optimist says its open, pessimisy
            ## says its ")"

            else:
                high +=1
                low -=1
            
            ## so if there are more *s then low can be negative
            if low < 0:
                low = 0
            if high < 0: ## too many close brackets
                return False
        return low == 0
