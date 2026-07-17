       
class TreeNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.next:
                curr.next[c] = TreeNode()
            curr = curr.next[c]
        
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        def recurse(node, word):
            if word == "":
                return node.isEnd

            c = word[0]

            if c  == ".":
                flag = False
                for key in node.next:
                    flag = flag or recurse(node.next[key], word[1:])
                return flag
            if c not in node.next:
                return False
            return recurse(node.next[c], word[1:])
               
        return recurse(self.head, word)