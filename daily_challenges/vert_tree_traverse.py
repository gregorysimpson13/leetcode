# Runtime: beats 98.99%
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        lookup = defaultdict(list)
        xmin, xmax = float('inf'), float('-inf')
        queue = [(root, 0)]
        while queue:
            new_queue = []
            nodes = sorted([(node.val, node, x) for node, x in queue], key=lambda x: x[0])
            for _, node, x in nodes:
                xmin, xmax = min(xmin, x), max(xmax, x)
                lookup[x].append(node.val)
                if node.left: new_queue.append((node.left, x-1))
                if node.right: new_queue.append((node.right, x+1))
            queue = new_queue
        return [lookup[i] for i in range(xmin, xmax+1)]