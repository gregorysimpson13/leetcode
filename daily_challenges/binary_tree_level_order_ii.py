# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None: return result
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if depth >= len(result):
                result.insert(0, [])
            result[0].append(node.val)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return result