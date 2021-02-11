# Runtime: O(n); 50.69%
# Space: O(1)
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def greater(node=root):
            if not node: return
            greater(node.right)
            node.val = self.sum = node.val + self.sum
            greater(node.left)
        greater()
        return root