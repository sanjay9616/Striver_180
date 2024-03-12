# Approach 1:  Using HasMap

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hasMap_s, hasMap_t = {}, {}
        for i in s:
            if(i in hasMap_s):
                hasMap_s[i] += 1
            else:
                hasMap_s[i] = 1
        for i in t:
            if(i in hasMap_t):
                hasMap_t[i] += 1
            else:
                hasMap_t[i] = 1
        return hasMap_s == hasMap_t

# Time Coplexicity = O(N + N) = O(N) => Result = Success
# Space Complexity = O(N + N) = O(N)