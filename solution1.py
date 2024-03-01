# Approach 1: Using Recursion

class Solution:
	def subsetSums(self, arr, N):
		def subSum(ind, sum):
            if ind == len(arr):
                ans.append(sum)
                return
            subSum(ind+1,sum)
            subSum(ind+1,sum+arr[ind])
        ans = []
        subSum(0, 0)
        return sorted(ans)

# Time Coplexicity = O(2^N) => Result = Success
# Space Complexity = O(N)
