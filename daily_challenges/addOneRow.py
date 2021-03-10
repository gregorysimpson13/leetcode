# Runtime: O(n); beats 82.23%
# Space: O(1)
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dummy = TreeNode(left=root)
        def addrow(node=dummy,depth=1):
            if not node: return
            if depth == d:
                node.right = TreeNode(val=v, right=node.right)
                node.left = TreeNode(val=v, left=node.left)
                return
            addrow(node.left, depth+1); addrow(node.right, depth+1)
        addrow()
        return dummy.left