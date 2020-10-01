# Runtime: O(nlogn); beats 97.7%
# Space: O(n)

from bisect import bisect_left
class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        i = bisect_left(self.times, t-3000)
        return len(self.times) - i