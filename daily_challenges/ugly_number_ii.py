class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        ugly_numbers_set = set(ugly_numbers)
        i, k, j = 0, 0, 0
        while n > len(ugly_numbers):
            next_ugly = min(ugly_numbers[i] * 2, ugly_numbers[k] * 3, ugly_numbers[j] * 5)
            if next_ugly not in ugly_numbers_set:
                ugly_numbers.append(next_ugly)
            ugly_numbers_set.add(next_ugly)
            if next_ugly == ugly_numbers[i] * 2:
                i = i + 1
            elif next_ugly == ugly_numbers[k] * 3:
                k = k + 1
            elif next_ugly == ugly_numbers[j] * 5:
                j = j + 1
        return ugly_numbers[n-1]