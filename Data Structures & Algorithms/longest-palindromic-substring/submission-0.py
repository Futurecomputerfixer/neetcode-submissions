class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            nonlocal res
            if l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1] if (r-l+1) > len(res) else res
                expand(l-1, r+1)

        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return res