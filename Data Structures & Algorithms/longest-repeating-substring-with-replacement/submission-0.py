class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        max_length = 0
        freq_map = {}
        max_freq = 0

        while end < len(s):
            # Step 1: Add s[end] to freq_map
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            # Step 2: Update max_freq (most frequent char in current window)
            max_freq = max(max_freq, freq_map[s[end]])

            # Step 3: Check if window is valid
            window_size = end - start + 1
            if (window_size - max_freq) > k:
                # Too many replacements needed → shrink window from left
                freq_map[s[start]] -= 1
                start += 1  # move the window
            else:
                # Valid window → update max_length
                max_length = max(max_length, window_size)

            # Step 4: Move end forward
            end += 1

        return max_length
