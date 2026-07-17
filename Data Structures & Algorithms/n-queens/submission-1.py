class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        diagLeft = set()
        diagRight = set()
        vert = set()

        def bt(row):
            if row == n:
                res.append(["".join(R) for R in board])
                return
            
            for col in range(n):
                if col in vert or row+col in diagRight or row-col in diagLeft:
                    continue
                vert.add(col)
                diagRight.add(row+col)
                diagLeft.add(row-col)

                board[row][col] = "Q"

                bt(row+1)

                vert.discard(col)
                diagRight.discard(row+col)
                diagLeft.discard(row-col)
                board[row][col] = "."
        
        bt(0)
        return res