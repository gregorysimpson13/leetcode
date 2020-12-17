# Runtime: O(n); beats 56.10%
# Space: O(1)
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepest(node=root, depth=0):
            if not node: return node, depth
            left_node, l_val = deepest(node.left, depth+1)
            right_node, r_val = deepest(node.right, depth+1)
            if l_val == r_val: return node, l_val
            return (left_node, l_val) if l_val > r_val else (right_node, r_val)
        return deepest()[0]