### Approach 1: Merge Overlapping Intervals using Sorting (Optimized Approach)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals)
        res = [sortedIntervals[0]]
        for i in range(1, len(sortedIntervals)):
            if(sortedIntervals[i][0] > res[-1][1]):
                res.append(sortedIntervals[i])
            elif(sortedIntervals[i][0] <= res[-1][1] and sortedIntervals[i][1] > res[-1][1]):
                res[-1][1] = sortedIntervals[i][1]
        return res



# Transpose then Reverse individual rows
# Time Coplexicity = (n * log(n)) = O(n * log(n)) => Result = Success
# Space Complexity = O(N)
