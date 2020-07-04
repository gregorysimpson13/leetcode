def prisonAfterNDays(cells, N: int):
    mod = N % 14
    for _ in range(mod):
        prev_value = cells[0]
        cells[0] = 0
        for i in range(1, len(cells)-1):
            tmp_value = cells[i]
            cells[i] = 1 if prev_value == cells[i+1] else 0
            prev_value = tmp_value
        cells[-1] = 0
    return cells

# print(prisonAfterNDays([0,1,0,1,1,0,0,1], 6))
# print(prisonAfterNDays([0,1,0,1,1,0,0,1], 454))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0], 454))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0], 6))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
# print(prisonAfterNDays([0,0,0,1,0,0,1,0], 9999999999))
# print(prisonAfterNDays([0,0,0,1,0,0,1,0], 5))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000014))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 0))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 14))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 28))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 29))
print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
print(prisonAfterNDays([1,0,0,1,0,0,0,1], 826))



# [0,0,1,1,1,1,1,0] - 100M

# 
# [0,1,1,0,1,1,1,0]
