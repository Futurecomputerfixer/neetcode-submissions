class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(s, openN, closeN):
            if len(s) == 2 * n:
                res.append(s)
                return
            if openN < n:
                bt(s + "(", openN + 1, closeN)
            if closeN < openN:
                bt(s + ")", openN, closeN + 1)
        
        bt("", 0, 0)
        return res