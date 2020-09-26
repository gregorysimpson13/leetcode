# Runtime: O(nlogn); beats 80.25%
# Space: O(n); beats 22.22%
​
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        bucket = defaultdict(list)
        for word, val in Counter(words).items():
            bucket[val].append(word)
        i, res, keys = 0, [], sorted(bucket.keys(), reverse=True)
        while len(res) < k:
            res.extend(sorted(bucket[keys[i]]))
            i += 1
        return res[:k]