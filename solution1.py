# Approach 1: DFS

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def clone(node):
            if(node in old_to_new):
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))
            return copy
        return clone(node) if node else None

# Time Coplexicity = O(V + E) => Result = Success
# Space Complexity = O(V)
