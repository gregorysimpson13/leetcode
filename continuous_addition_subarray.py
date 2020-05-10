def find_max(arr):
    max_sum_global = arr[0]
    max_sum_current = arr[0]
    for i in range(1,len(arr)):
        max_sum_current = max(arr[i], arr[i]+max_sum_current)
        max_sum_global = max(max_sum_global, max_sum_current)
    return max_sum_global


print(find_max([1,2,3,4,8,-12,10]), 18)
print(find_max([-2,1,-3,4,-1,2,1,-5,4]), 6)