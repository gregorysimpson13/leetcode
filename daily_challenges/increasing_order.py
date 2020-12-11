# Runtime: O(n); beats 59.30%
# Space: O(n)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        arr = []
        def inorder(node=root):
            if not node: return
            inorder(node.left); node.left = None
            arr.append(node)
            inorder(node.right); node.right = None
        inorder()
        for i in range(1, len(arr)):
            arr[i-1].right = arr[i]
        return arr[0]