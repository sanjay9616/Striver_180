### Approach 1: Brute Force Approach using Sorting

A simple approach is to start from the first interval and compare it with all other intervals for overlapping, if it overlaps with any other interval, then remove the other interval from the list and merge the other into the first interval. Repeat the same steps for the remaining intervals after the first. This approach cannot be implemented in better than O(n^2) time.


| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N<sup>2</sup>)  | O(N)              |

### Approach 2: Merge Overlapping Intervals using Sorting (Optimized Approach)

Same Approah as 1st Approach

| Algorithm                       | Time Complexity   | Space Complexity  |
|-------------------------------- | ----------------- | ----------------- |
| Brute Force (Optimized - time)  | O(N*log(N))       | O(N)              |

### Approach 3: Merge Overlapping Intervals using Sorting (Space Optimized)

The above solution requires O(n) extra space for the stack. We can avoid the use of extra space by doing merge operations in place. Below are detailed steps.

| Algorithm                                  | Time Complexity   | Space Complexity |
|------------------------------------------- | ----------------- | ---------------- |
| Brute Force (Optimized - time & space)     | O(N*log(N))       | O(1)             |
