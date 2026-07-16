class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        flag = [False]
        visited = set()
        def bt(state, i, j):
            idx = i*m+j
            if idx in visited: return
            
            if 0 <= i and i < n and j >= 0 and j < m:
                state += board[i][j]
                if state[-1] != word[len(state)-1]: return
            else:return
            if state == word:
                flag[0] = True
            elif len(state) != len(word):
                visited.add(idx)
                bt(state, i+1, j)
                bt(state, i, j+1)
                bt(state, i-1, j)
                bt(state, i, j-1)
            
                visited.discard(idx)

        for i in range(len(board)):
            for j in range(len(board[0])):
                bt("", i, j)
        return flag[0]
