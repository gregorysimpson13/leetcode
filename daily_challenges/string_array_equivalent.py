class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x1 = x2 = y1 = y2 = 0
        while x1 < len(word1):
            if x2 == len(word1[x1]): x1, x2 = x1+1, 0
            if y2 == len(word2[y1]): y1, y2 = y1+1, 0
            l1 = word1[x1][x2] if x1 < len(word1) else ""
            l2 = word2[y1][y2] if y1 < len(word2) else ""
            if l1 != l2: return False
            x2+=1; y2+=1
        return True