# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        order_dict = defaultdict(list)
        queue = [(root, 0)]
        min_x, max_x = float('inf'), float('-inf')
        while queue:
            tmp_queue = []
            x_coords = defaultdict(list)
            for item in queue:
                node, pos_x = item
                x_coords[pos_x].append(node.val)
                x_coords[pos_x].sort()
                min_x, max_x = min(min_x, pos_x), max(max_x, pos_x)
                if node.left: tmp_queue.append((node.left, pos_x - 1))
                if node.right: tmp_queue.append((node.right, pos_x + 1))
            for key, val in x_coords.items(): order_dict[key].extend(val)
            queue = tmp_queue
        return [order_dict[i] for i in range(min_x, max_x + 1)]