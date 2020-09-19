class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        def get_digit(val):
            if val > high: return
            if low <= val <= high: result.append(val)
            last_digit = val % 10
            if last_digit != 9: get_digit((val*10)+last_digit+1)
        [get_digit(i) for i in range(1,9)]
        return sorted(result)