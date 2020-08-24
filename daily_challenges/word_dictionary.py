class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.letter_lookup = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        local_lookup = self.letter_lookup
        for letter in word+'\0':
            if letter not in local_lookup:
                local_lookup[letter] = {}
            local_lookup = local_lookup[letter]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        word = word + '\0'
        def searchWord(index, lookup):
            if not lookup: return False
            for i in range(index, len(word)):
                if word[i] == '.':
                    retVal = False
                    for vals in lookup.values(): 
                        retVal |= searchWord(i+1, vals)
                    return retVal
                elif word[i] in lookup:
                    lookup = lookup[word[i]]
                elif word[i] not in lookup:
                    return False
            return True
        return searchWord(0, self.letter_lookup)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("word")
# param_2 = obj.search("word")
# print(obj.search("wor."))
# print(obj.search("w.r."))
# print(param_2)


word_dict = WordDictionary()
word_dict.addWord("a")
word_dict.addWord("a")
print(word_dict.search("."), True)
print(word_dict.search("a"), True)
print(word_dict.search("aa"), False)
print(word_dict.search("a"), True)
print(word_dict.search(".a"), False)
print(word_dict.search("a."), False)

