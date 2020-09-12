class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [arr for arr in combinations(range(1,min(n, 10)), k) if sum(arr) == n]