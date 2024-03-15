# Approach 1: Using DFS

from typing import List


def dfs(root, result: List[str], curr: str) -> None:
    if root is None:
        return
    if len(curr) == 0:
        curr += str(root.data)
    else:
        curr += " " + str(root.data)
    if root.left is None and root.right is None:
        result.append(curr)
    dfs(root.left, result, curr)
    dfs(root.right, result, curr)


def allRootToLeaf(root) -> List[str]:
    result = []
    dfs(root, result, "")
    return result


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
