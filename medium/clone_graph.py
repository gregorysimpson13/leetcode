# https://leetcode.com/problems/clone-graph/





class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited_dict = {}
        
        def clone(node):
            if node == None:
                return node
            
            if node.val in visited_dict:
                return visited_dict[node.val]
            
            curr_node = Node(node.val)
            visited_dict[curr_node.val] = curr_node
            
            for n in node.neighbors:
                curr_node.neighbors.append(clone(n))
             
                    
            return curr_node
        return clone(node)