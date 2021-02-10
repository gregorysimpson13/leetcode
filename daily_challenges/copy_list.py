# Runtime: O(n); beats 36.34%
# Space: O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {None: None}
        def copy(n:'Node'=head):
            if n in lookup: return lookup[n]
            lookup[n] = Node(n.val)
            lookup[n].next, lookup[n].random = copy(n.next), copy(n.random)
            return lookup[n]
        return copy()