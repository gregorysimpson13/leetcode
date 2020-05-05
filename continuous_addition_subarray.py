def find_max(arr):
    max_sum = arr[0]
    for i in range(1,len(arr)):
        max_sum = max(arr[i], arr[i]+max_sum)
    return max_sum


print(find_max([1,2,3,4,-12,10]))