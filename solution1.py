# Approach 1: DFS (Implement Again)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        color1 = image[sr][sc]
        if (color1 == color):
            return image

        def dfs(r, c):
            if (image[r][c] == color1):
                image[r][c] = color
                if (r >= 1):
                    dfs(r-1, c)
                if (r < n-1):
                    dfs(r+1, c)
                if (c >= 1):
                    dfs(r, c-1)
                if (c < m-1):
                    dfs(r, c+1)
        dfs(sr, sc)
        return image

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
