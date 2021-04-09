class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        l = {l:i for i,l in enumerate(order)}; l[''] = -1
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(max(len(word1), len(word2))):
                l1 = word1[j] if j < len(word1) else ''
                l2 = word2[j] if j < len(word2) else ''
                if l[l2] < l[l1]: return False
                if l[l1] < l[l2]: break
        return True
