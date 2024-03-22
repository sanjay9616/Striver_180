# Approach 1: DFS

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False]*V
        visited[0] = True
        q = [0]
        result = []
        while q:
            temp = q.pop(0)
            if temp not in result:
                result.append(temp)
            for i in adj[temp]:
                if visited[i] == False:
                    visited[i] == True
                    q.append(i)
        return result

# Time Coplexicity = O(V + E) => Result = TLE
# Space Complexity = O(V)

# ---------------- Using Python Fnction ----------------- #

from typing import List
from queue import Queue
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q = Queue(maxsize=V)
        res = []
        visited = [False]*V
        q.put(0)
        visited[0] = True
        while not q.empty():
            temp = q.get()
            res.append(temp)
            for e in adj[temp]:
                if visited[e] == False:
                    q.put(e)
                    visited[e] = True
        return res

# Time Coplexicity = O(V + E) => Result = Success
# Space Complexity = O(V)
