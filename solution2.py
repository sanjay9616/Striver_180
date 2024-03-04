# Approach 1: Using Max-Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hasMap = {}
        for i in nums:
            if (i in hasMap):
                hasMap[i] += 1
            else:
                hasMap[i] = 1
        heap = [[value, key] for key, value in hasMap.items()]
        res = []
        for i in heapq.nlargest(k, heap):
            res.append(i[1])
        return res

# Time Coplexicity = O(K log D + D log D) => Result = Success, where D is count of distinct element
# Space Complexity = O(D)
