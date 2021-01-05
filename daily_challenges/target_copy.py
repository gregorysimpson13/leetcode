class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        o_queue, c_queue = [original], [cloned]
        while o_queue:
            o, c = o_queue.pop(0), c_queue.pop(0)
            if o == target: return c
            if o.left: o_queue.append(o.left); c_queue.append(c.left)
            if o.right: o_queue.append(o.right); c_queue.append(c.right)
        return None