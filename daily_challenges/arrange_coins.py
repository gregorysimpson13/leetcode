class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        coins = n
        for i in range(n):
            row_number = i + 1
            coins = coins - row_number
            if coins < 0:
                return row
            row = row_number
        return row