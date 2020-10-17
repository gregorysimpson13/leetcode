# Runtime: O(n^2)
# Space: O(n)
​
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        series, res = set(), set()
        for i in range(len(s)-9):
            sequence = s[i:i+10]
            if sequence in series: res.add(sequence)
            series.add(sequence)
        return list(res)