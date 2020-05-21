# 152. Maximum Product Subarray - MEDIUM
# https://leetcode.com/problems/maximum-product-subarray/

def find_max_subarray(arr):
    maximum_global, maximum_current = arr[0], arr[0]
    local_minimum_current, minimum_current = arr[0], arr[0]
    for i in range(1,len(arr)):
        local_minimum_current = min(arr[i], arr[i] * maximum_current, arr[i] * minimum_current)
        maximum_current = max(arr[i], arr[i] * maximum_current, arr[i] * minimum_current)
        minimum_current = local_minimum_current
        maximum_global = max(maximum_global, maximum_current)
    return maximum_global


print(find_max_subarray([1,2,3]), 6)
print(find_max_subarray([1,10,2,-20]), 20)
print(find_max_subarray([1,10,2,-20,4]), 20)
print(find_max_subarray([1,10,2,-20,5,-10]), 2000)
print(find_max_subarray([2,3,-2,4]), 6)
print(find_max_subarray([-2,0,-1]), 0)
print(find_max_subarray([-4,-3,-2]), 12)