class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].add(word)
        queue = [(1, beginWord)]
        visited = set()
        while queue:
            trans, word = queue.pop(0)
            if word in visited: continue
            visited.add(word)
            if endWord == word: return trans
            for i in range(len(word)):
                queue.extend([(trans+1, w) for w in patterns[word[:i] + "*" + word[i+1:]]])
        return 0
                
