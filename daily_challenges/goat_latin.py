#Runtime: O(n)
#Space: O(n)

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set(["a","e","i","o","u"])
        word_arr = []
        for i, word in enumerate(S.split(' ')):
            word_transform = word if word[0].lower() in vowels else word[1:] + word[0]
            word_arr.append(word_transform + "ma" + "a" * (i+1))
        return " ".join(word_arr)