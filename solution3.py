# Approach 3: Optimal Approach
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans,s=0,set(nums)
        for i in s:
            if(i-1 in s):
                continue
            c=1
            while(i+1 in s):
                c+=1
                i+=1
            ans=max(ans,c)
        return ans

# Optimal Approach
# Time Coplexicity = O(N) OR O(N^2) => Result = Success
# Space Complexity = O(1)