# Runtime: O(n log n); beats 26.08%
# Space: O(n)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        index_lookup = defaultdict(list)
        for i, n in enumerate(arr[1:], 1):
            if i + 1 < len(arr) and arr[i-1] == n and arr[i+1] == n: continue
            index_lookup[n].append(i)
        heap, visited = [(0,0)], set()
        while heap:
            hops, index = heappop(heap)
            if index == len(arr) - 1: return hops
            if index in visited: continue
            visited.add(index)
            hops = hops + 1
            heappush(heap, (hops, index+1))
            if index != 0 and index-1 not in visited: heappush(heap, (hops, index-1))
            for i in index_lookup[arr[index]]: 
                if i not in visited: heappush(heap, (hops, i))