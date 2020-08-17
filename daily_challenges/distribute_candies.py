
from typing import List

# Runtime 40ms; Beats 73%
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give_amount, index = 0, 0
        while candies > 0:
            give_amount = give_amount + 1 if candies >= give_amount + 1 else candies
            result[index % num_people] = result[index % num_people] + give_amount
            candies = candies - give_amount
            index = index + 1
        return result


# Runtime 36ms; Beats 87.9
# Memory 13.8 MB; Beats 87.2%
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give_amount = 0
        while candies > 0:
            for i in range(num_people):
                give_amount = give_amount + 1 if candies >= give_amount + 1 else candies
                result[i] = result[i] + give_amount
                candies = candies - give_amount
        return result