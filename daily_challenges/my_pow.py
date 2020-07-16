class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {0:1}
        def my_pow(x, n):
            nonlocal cache
            if n < 0:
                x = 1 / x
                n = -1 * n
            if n in cache:
                return cache[n]
            cache[n] = x * my_pow(x, n-1) if n % 2 != 0 else my_pow(x, n//2) * my_pow(x, n//2)
            return cache[n]
        return my_pow(x,n)

class Solution1:
    def myPower(self, x: float, n: int) -> float:
        cache = {0:1}
        def helper(x, n):
            if n < 0:
                x = 1 / x
                n = -1 * n
            if n in cache:
                if n != 0: print('cache hit', n)
                return cache[n]
            cache[n] = x * self.myPow(x, n-1)
            print(cache)
            return cache[n]
        # helper(x,n)
        # print(cache)
        return helper(x,n)



args = [(2.0, 10), (2.0, -2), (2.1,3), (1.00001, 123456), (0.00001, 2147483647)]
for x, n in args:
    print(Solution().myPow(x, n), x**n)