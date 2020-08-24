#Runtime: O(nk); beats 65.9%
#Space: O(k); beats 51.68%


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        result = [1]
        for _ in range(rowIndex):
            tmp = 1
            for i in range(1, len(result)):
                 result[i], tmp = tmp + result[i], result[i]
            result.append(1)
        return result