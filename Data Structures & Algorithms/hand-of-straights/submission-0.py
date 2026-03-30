from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1. Quick Failure Check: Total cards must be divisible by group size
        if len(hand) % groupSize != 0:
            return False

        # 2. Count frequency of each card
        count = Counter(hand)

        # 3. Sort the unique cards
        # We MUST process from smallest to largest because the smallest card
        # currently available HAS to be the start of a sequence.
        sorted_keys = sorted(count.keys())

        for card in sorted_keys:
            # If the current card's count is 0, it was already used up
            # as part of a previous sequence (e.g., 2 used by a sequence starting at 1).
            if count[card] > 0:
                
                # This is the "Batch Processing" logic
                # We need to start 'start_count' number of sequences right now.
                start_count = count[card]
                
                # Check the next 'groupSize' consecutive numbers
                for i in range(groupSize):
                    current_card = card + i
                    
                    # If we don't have enough of the next card to continue the sequence
                    if count[current_card] < start_count:
                        return False
                    
                    # Deduct the cards used
                    count[current_card] -= start_count
                    
        return True