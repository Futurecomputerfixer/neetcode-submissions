class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        digitToLetters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []

        def bt(state, idx):
            if idx == len(digits):
                res.append("".join(state))
                return
            
            letters = digitToLetters[digits[idx]]
            for c in letters:
                state.append(c)
                bt(state, idx+1)
                state.pop()
        
        bt([], 0)

        return res