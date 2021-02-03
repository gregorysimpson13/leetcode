# Runtime: O(n); beats 16.11%
# Space: O(1)
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root: return None
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        if low <= root.val <= high: root.left = left; root.right = right; return root
        if root.val < low: return right
        return left