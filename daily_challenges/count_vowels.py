class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = ["a", "e", "i", "o", "u"]
        def count(i=0,curr=[]):
            if len(curr) == n: return 1
            c = 0
            for j in range(i,len(arr)):
                curr.append(arr[j]); c += count(j,curr); curr.pop()
            return c
        return count()