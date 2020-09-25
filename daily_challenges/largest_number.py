class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: max(list(str(x))), reverse=True)
        return str(int("".join([str(n) for n in nums])))

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_list = [list(str(n)) for n in nums]
        def merge_sort(i, j):
            if i > j: return []
            if i == j: return nums_list[i]
            m = (i+j) // 2
            left, right = merge_sort(i,m), merge_sort(m+1, j)
            l, r, res = 0, 0, []
            while l < len(left) and r < len(right):
                left_val, right_val = left[l], right[r]
                if left_val[0] == right_val[0]:
                    for idx in range(1, max(len(left_val), len(right_val))):
                        if idx == len(left_val):
                            res.append(left_val); l += 1; break
                        elif idx == len(right_val):
                            res.append(right_val); r+= 1; break
                        if left_val[idx] > right_val[idx]: res.append(left_val); l += 1
                        if right_val[idx] > left_val[idx]: res.append(right_val); r += 1
                elif left_val[0] < right_val[0]:
                    res.append(right_val); r += 1
                elif right_val[0] < left_val[0]:
                    res.append(left_val); l += 1
            if l < len(left): res.extend(left[l:])
            if r < len(right): res.extend(right[r:])
            return res
        return merge_sort(0, len(nums_list) - 1)
        


def largestNumber(self, nums: List[int]) -> str:
        nums_list = [list(str(n)) for n in nums]
        compare = lambda x, y: x if nums_list[x] + nums_list[y] > nums_list[y] + nums_list[x] else y if nums_list[x] + nums_list[y] < nums_list[y] + nums_list[x] else x
        for i in range(len(nums_list)):
            max_idx = i
            for j in range(i+1, len(nums_list)):
                max_idx = compare(max_idx, j)
            nums_list[max_idx], nums_list[i] = nums_list[i], nums_list[max_idx]
        nums_list = ["".join(n) for n in nums_list]
        return str(int("".join(nums_list)))