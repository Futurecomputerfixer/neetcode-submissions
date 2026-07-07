class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = defaultdict(set), defaultdict(set),defaultdict(set)

        n = len(board)

        for i in range(n):
            for j in range(n):
                c = board[i][j]
                if c == ".": continue
                sq = (i//3)*3+(j//3)
                if c in row[i] or c in col[j] or c in square[sq]: return False

                row[i].add(c)
                col[j].add(c)
                square[sq].add(c)
        
        return True