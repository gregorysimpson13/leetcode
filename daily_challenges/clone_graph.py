# Runtime: O(n)
# Space: O(n)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        lookup = {}
        def clone(node):
            if node.val in lookup: return lookup[node.val]
            newNode = Node(node.val)
            lookup[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(clone(neighbor))
            return newNode
        return clone(node)