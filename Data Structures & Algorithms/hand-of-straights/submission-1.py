class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        
        inventory = Counter(hand)
        unique_ele = sorted(inventory.keys())

        for ele in unique_ele:
            req_count = inventory[ele]

            if req_count > 0:
                for next_ele in range(ele,ele+groupSize):
                    if inventory[next_ele]<req_count:
                        return False
                    
                    inventory[next_ele] -= req_count
        return True