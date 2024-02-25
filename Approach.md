### Approach 1: Brute Force

A simple solution is consider every subarray and count 1’s in every subarray. Finally return size of largest subarray with all 1’s. An efficient solution is traverse array from left to right. If we see a 1, we increment count and compare it with maximum so far. If we see a 0, we reset count as 0.

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N)              | O(1)              |



