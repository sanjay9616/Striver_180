# Approach 1: Brute Force (Using Hash map)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasMap = {}
        for i in nums:
            if (i in hasMap):
                hasMap[i] += 1
            else:
                hasMap[i] = 1
        temp = []
        for i in hasMap:
            temp.append([i, hasMap[i]])
        temp.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(N + N) = O(N)
