# Approach 1:  Using HasMap (Space Optimized)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasMap = {}
        for i in s:
            if(i in hasMap):
                hasMap[i] += 1
            else:
                hasMap[i] = 1
        for i in t:
            if(i in hasMap):
                hasMap[i] -= 1
            else:
                hasMap[i] = 1
        for i in hasMap:
            if(hasMap[i] != 0):
                return False
        return True

# Time Coplexicity = O(N + N + N) = O(N) => Result = Success
# Space Complexity = O(N)