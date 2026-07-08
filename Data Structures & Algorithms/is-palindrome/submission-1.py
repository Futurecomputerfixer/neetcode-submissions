class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(c):
            c = ord(c)
            return ord("A") <= c <= ord("Z") or ord("a") <= c <= ord("z") or ord("0") <= c <= ord("9")

        i, j = 0, len(s)-1
        while i <= j:
            while i < j and not isAlphaNumeric(s[i].lower()):
                    i += 1
            while j > i and not isAlphaNumeric(s[j].lower()):
                    j -= 1
            
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
        return True
        