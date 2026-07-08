class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in check:
                res = max(res, r-l)
                while s[r] in check:
                    check.remove(s[l])
                    l+=1


            check.add(s[r])
            res = max(res, len(check))

            r += 1
            
        return res