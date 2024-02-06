### Approach 1: Brute Force Approach using Sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def bubbleSort(Arr):
            n = len(Arr)
            for i in range(n):
                for j in range(n-i-1):
                    if (Arr[j][0] > Arr[j+1][0]):
                        Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
            return Arr
        sortedIntervals = bubbleSort(intervals)
        res = [sortedIntervals[0]]
        for i in range(1, len(sortedIntervals)):
            if (sortedIntervals[i][0] > res[-1][1]):
                res.append(sortedIntervals[i])
            elif (sortedIntervals[i][0] <= res[-1][1] and sortedIntervals[i][1] > res[-1][1]):
                res[-1][1] = sortedIntervals[i][1]
        return res


# Brute Force Approach
# Time Coplexicity = (n*n) = O(n^2) => Result = Success
# Space Complexity = O(n)
