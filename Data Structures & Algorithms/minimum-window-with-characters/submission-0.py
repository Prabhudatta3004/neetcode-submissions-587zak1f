from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        freq_t = Counter(t)      # target char frequencies
        freq_window = {}         # current window freq
        have, need = 0, len(freq_t)
        res = [-1, -1]           # store [left, right] bounds of best window
        res_len = float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            freq_window[ch] = freq_window.get(ch, 0) + 1

            # If current char count matches target char count -> we’ve satisfied one char type
            if ch in freq_t and freq_window[ch] == freq_t[ch]:
                have += 1

            # When all target chars are matched
            while have == need:
                # Update result if this window is smaller
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Try shrinking from left
                freq_window[s[left]] -= 1
                if s[left] in freq_t and freq_window[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
