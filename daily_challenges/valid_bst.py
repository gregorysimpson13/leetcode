# Runtime: O(n); beats 65.88%
# Space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.lastVal = float('-inf')
        def inorder(node=root):
            if not node: return True
            if not inorder(node.left): return False
            if self.lastVal >= node.val: return False
            self.lastVal = node.val
            return inorder(node.right)
        return inorder()