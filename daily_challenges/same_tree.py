# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_queue, q_queue = [p], [q]
        while p_queue or q_queue:
            if not q_queue or not p_queue:
                return False
            q_node, p_node = q_queue.pop(0), p_queue.pop(0)
            if not q_node and not p_node:
                continue
            if not q_node or not p_node or (q_node.val != p_node.val):
                return False
            q_queue.append(q_node.left)
            q_queue.append(q_node.right)
            p_queue.append(p_node.left)
            p_queue.append(p_node.right)
        return True


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            q_node, p_node = queue.pop(0)
            if not q_node and not p_node:
                continue
            if not q_node or not p_node or (q_node.val != p_node.val):
                return False
            queue.append((q_node.left, p_node.left))
            queue.append((q_node.right, p_node.right))
        return True