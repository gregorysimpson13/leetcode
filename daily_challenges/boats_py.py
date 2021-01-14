# Runtime: O(nlogn)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c, l, r = 0, 0, len(people) - 1
        while l <= r:
            while l < r and people[r] + people[l] > limit: c, r = c + 1, r - 1
            if l == r: c = c + 1; break
            else: c, l, r = c + 1, l + 1, r - 1
        return c