class Solution:
    def solve(self, board: List[List[str]]) -> None:

        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if not (i >= 0 and i < n and j >= 0 and j < m) or board[i][j] != 'O':
                return 
            board[i][j] = 'T'  
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and board[i][j] == 'O':
                    dfs(i, j)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        
