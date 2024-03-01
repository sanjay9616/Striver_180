# Approach 1: Efficient Iterative Method

class Solution:
	def subsetSums(self, arr, N):
		res = [0]
    	for i in range(N):
    		for j in range(len(res)):
    			res.append(res[j] + arr[i])
    	return sorted(res)

# Time Coplexicity = O(2^N) => Result = Success
# Space Complexity = O(1)