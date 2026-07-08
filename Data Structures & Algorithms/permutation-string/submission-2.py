class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        check = [0]*26
        window = [0]*26

        for c in s1:
            check[ord(c)-ord('a')] +=1
        
        for r in range(len(s2)):
            window[ord(s2[r])-ord('a')] +=1

            diff = r-len(s1)
            if diff >= 0:
                window[ord(s2[diff])-ord('a')] -= 1

            if window == check: return True
        
        return False
            