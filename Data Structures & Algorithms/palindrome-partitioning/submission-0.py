class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(string):
            return string == string[::-1]
        
        res = []

        def bt(state, start):
            if start == len(s):
                res.append(state[:])
                return
            
            for i in range(start, len(s)):
                if isPal(s[start:i+1]):
                    state.append(s[start:i+1])
                    bt(state, i+1)
                    state.pop()
            
        bt([], 0)

        return res
