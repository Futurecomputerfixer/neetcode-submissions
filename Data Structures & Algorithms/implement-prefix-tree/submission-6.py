class TreeNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.next:
                curr.next[c] = TreeNode()
            curr = curr.next[c]
        
        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr.next:
                return False
            curr = curr.next[c]
               
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.next:
                return False
            curr = curr.next[c]
               
        return True
        
        