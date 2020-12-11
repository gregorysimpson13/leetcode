# Runtime: O(n); beats 46.2%
# Space: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        seen = set(queue)
        while queue:
            i = queue.pop(0)
            if arr[i] == 0: return True
            next_right, next_left = i + arr[i], i - arr[i]
            if next_left >= 0 and next_left not in seen: queue.append(next_left); seen.add(next_left)
            if next_right < len(arr) and next_right not in seen: queue.append(next_right); seen.add(next_right)
        return False