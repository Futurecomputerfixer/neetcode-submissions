class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        check = [0]*200
        window = [0]*200
        def verify(l1,  l2): 
            for i in range(200):
                if l1[i] > window[i]:
                    return False
            return True

        minimum = len(s)
        res = ""

        for c in t:
            check[ord(c)-ord('a')] +=1
        
        l = 0
        for r in range(len(s)):
            window[ord(s[r])-ord('a')] +=1
            while verify(check, window):
                if r-l+1 <= minimum:
                    minimum = r-l+1
                    res = s[l:r+1]
                window[ord(s[l])-ord('a')] -=1
                l+=1 
            
            
        
        return res
            