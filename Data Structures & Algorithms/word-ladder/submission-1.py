class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        steps = 1
        visited = set([beginWord])
        if endWord not in wordList: return 0


        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return steps

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i]+c+word[i+1:]
                        if newWord in wordList and newWord not in visited:
                            visited.add(newWord)
                            q.append(newWord)
                
            steps += 1
        
        return 0
