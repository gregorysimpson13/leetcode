# Runtime O(k^n); beats 38%
# Space O(k*n)



class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.iterator = 0
        self.combinationList = []
        self.createCombinations()

    def next(self) -> str:
        tmp = self.combinationList[self.iterator] if self.hasNext() else None
        self.iterator = self.iterator + 1
        return tmp

    def hasNext(self) -> bool:
        return self.iterator < len(self.combinationList)
        
    def createCombinations(self) -> None:
        @lru_cache(None)
        def combinations(i=0, string=""):
            if len(string) == self.combinationLength:
                self.combinationList.append(string)
            for j in range(i, len(self.characters)):
                combinations(j+1, string+self.characters[j])
        combinations()
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()