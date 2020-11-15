# Runtime: O(n); beats 56.74%
# Space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while queue:
            nodes, prevNode = [], None
            for node in queue:
                if prevNode: prevNode.next = node
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
                prevNode = node
            queue = nodes
        return root
