from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def retval(x):
            if x % 3 == 0 and x % 5 == 0: return "FizzBuzz"
            if x % 3 == 0: return "Fizz"
            if x % 5 == 0: return "Buzz"
            return str(x)
        return [retval(val) for val in range(1, n+1)]