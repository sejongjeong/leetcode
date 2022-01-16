class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(start: int, end: int) -> str:
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1 : end]

        if len(s) < 2 or s == s[::-1]:
            return s
        res = ""
        for i in range(len(s) - 1):
            res = max(res, expand(i, i + 1), expand(i, i + 2), key=len)
        return res
