# Approach 1: DFS

class Solution:
    def dfsOfGraph(self, V, adj):
        def dfs(v, visited, adj, result):
            visited[v] = True
            result.append(v)
            for u in adj[v]:
                if not visited[u]:
                    dfs(u, visited, adj, result)
        visited = [False] * V
        result = []
        dfs(0, visited, adj, result)
        return result

# Time Coplexicity = O(V + E) => Result = Success
# Space Complexity = O(V)
