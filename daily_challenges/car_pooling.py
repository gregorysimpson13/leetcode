# Runtime: O(n) beats 97.85
# Space: O(n) beats 60.88


from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carpool = defaultdict(int)
        for persons, start, end in trips:
            carpool[start] += persons; carpool[end] -= persons
        persons = 0
        for location in sorted(carpool.keys()):
            persons += carpool[location]
            if persons > capacity: return False
        return True