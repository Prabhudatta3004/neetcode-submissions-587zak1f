class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub):
            return sub == sub[::-1]

        s = ''.join(c.lower() for c in s if c.isalnum())

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # Try skipping either s[i] or s[j]
                return is_palindrome(s[i+1:j+1]) or is_palindrome(s[i:j])
            i += 1
            j -= 1
        return True
