# Approach 1: Using Heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(k)
