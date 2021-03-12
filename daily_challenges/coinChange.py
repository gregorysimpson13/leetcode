# Runtime: O(n^2); 32.16%
# Space: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return amount
        dp = defaultdict(lambda: float('inf')); dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c in dp: dp[i] = min(dp[i], dp[i-c]+1)
        return dp[amount] if dp[amount] != float('inf') else -1