class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        l = 0
        Freq = defaultdict(int)
        res = 0

        for r in range(len(s)):
            Freq[s[r]] += 1
            maxFreq = max(maxFreq, Freq[s[r]])

            if r-l+1 - maxFreq > k:
                Freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
            


