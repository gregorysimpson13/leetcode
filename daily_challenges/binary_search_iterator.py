# Runtime Beats 91.66%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.i = -1
        self.arr = []
        self.inorder(root)
		
    def inorder(self, node: TreeNode):
        if not node: return
        self.inorder(node.left); self.arr.append(node.val); self.inorder(node.right)

    def next(self) -> int:
        self.i = self.i + 1
        return self.arr[self.i]
        

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()