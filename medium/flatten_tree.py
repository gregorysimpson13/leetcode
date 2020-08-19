class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if not node: return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        if not root: return
        nodes = []
        preorder(root)
        curr = nodes.pop(0)
        while nodes:
            curr.left = None
            curr.right = nodes.pop(0)
            curr = curr.right
        