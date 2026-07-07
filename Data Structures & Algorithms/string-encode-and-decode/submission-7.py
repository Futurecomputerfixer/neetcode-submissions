class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if not strs: return ""
        for s in strs:
            res.append(str(len(s)))
            res.append(",")
        
        res.pop()
        res.append("#")
        res.extend(strs)
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        if not s: return []
        i = 0
        while s[i] != '#':
            i+=1
        
        size = s[:i].split(",")
        i+=1
        res = []
        for si in size:
            res.append(s[i:(i+int(si))])
            i += int(si)
        
        return res
