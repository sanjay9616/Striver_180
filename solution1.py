# Approach 1: Brute Force
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        m, n = len(version1), len(version2)
        i = j = 0
        while (i < m or j < n):
            revision1 = int(version1[i]) if (i < m) else 0
            revision2 = int(version2[j]) if (j < n) else 0
            if (revision1 < revision2):
                return -1
            if (revision1 > revision2):
                return 1
            i, j = i + 1, j + 1

        return 0

# Time Coplexicity = O(M + N) => Result = Success
# Space Complexity = O(1)
