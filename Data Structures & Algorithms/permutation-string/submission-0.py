class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        new_str = ""
        start = end = 0
        second_hash = [0] * 26

        # Creating the original hash map for s1
        og_hash = [0] * 26
        for s in s1:
            og_hash[ord(s) - ord('a')] += 1

        while end < len(s2):
            # Add the new character to new_str
            new_str += s2[end]

            if len(new_str) < window_size:
                end += 1
            elif len(new_str) == window_size:
                # Reset second_hash for the current window
                second_hash = [0] * 26
                for s in new_str:
                    second_hash[ord(s) - ord('a')] += 1
                if og_hash == second_hash:
                    return True

                # Slide the window by removing the first char of new_str
                new_str = new_str[1:]
                start += 1
                end += 1

        return False
