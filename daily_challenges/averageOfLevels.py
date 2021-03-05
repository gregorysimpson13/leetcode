# Runtime: O(n); beats 17.82%
# Space: O(n)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return [0]
        queue, ans = [(root,0)], []
        while queue:
            node, lvl = queue.pop(0)
            if lvl == len(ans): ans.append([])
            ans[lvl].append(node.val)
            if node.left: queue.append((node.left, lvl+1))
            if node.right: queue.append((node.right, lvl+1))
        return [statistics.mean(lvl) for lvl in ans]