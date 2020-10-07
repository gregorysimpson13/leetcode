# Runtime: O(log n); beats 99.26%
# Space: O(1)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if not root: return newNode
        prev, curr = None, root
        while curr:
            if val < curr.val:
                prev, curr = curr, curr.left
            else:
                prev, curr = curr, curr.right
        if val < prev.val: prev.left = newNode
        else: prev.right = newNode
        return root