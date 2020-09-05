# Runtime: O(n); beats 61.5%
# Space: O(n); beats 46.3%
from heapq import merge
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result_1 = []
        result_2 = []
        def get_elements(node: TreeNode, tree: int):
            if node == None: return
            get_elements(node.left, tree)
            if tree == 1: result_1.append(node.val)
            if tree == 2: result_2.append(node.val)
            get_elements(node.right, tree)
        get_elements(root1, 1); get_elements(root2, 2)
        return merge(result_1, result_2)
    