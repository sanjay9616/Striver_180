class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index = 0
        for i in range(1, len(intervals)):
            if (intervals[index][1] >= intervals[i][0]):
                intervals[index][1] = max(intervals[index][1], intervals[i][1])
            else:
                index = index + 1
                intervals[index] = intervals[i]
        return intervals[:index+1]


# Merge Overlapping Intervals using Sorting (time & Space Optimized)
# Time Coplexicity = (n * log(n)) = O(n*logg(n)) => Result = Success
# Space Complexity = O(1)
