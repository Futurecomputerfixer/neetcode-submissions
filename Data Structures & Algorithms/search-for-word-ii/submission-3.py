class TreeNode:
    def __init__(self):
        self.next = {}
        self.isWord = False

    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TreeNode()

        for word in words:
            curr = head
            for c in word:
                if c not in curr.next:
                    curr.next[c] = TreeNode()
                curr = curr.next[c]
            
            curr.isWord = True
            curr.word = word
        
        res = []
        rows = len(board)
        cols = len(board[0])
        visited = set()
        root = head
        def dfs(r, c, node):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or board[r][c] not in node.next):
                return

            char = board[r][c]
            nextNode = node.next[char]

            if nextNode.isWord:
                res.append(nextNode.word)
                nextNode.isWord = False  # avoid adding the same word twice

            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, nextNode)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
        
