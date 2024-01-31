### Approach 1: Time Complexity O(N<sup>2</sup>)

| Algorithm       | Time Complexity   | Space Complexity (Worst Case) |
|---------------- | ----------------- | ----------------------------- |
| Bubble Sort     | O(N<sup>2</sup>)  | O(1)                          |
| Selection Sort  | O(N<sup>2</sup>)  | O(1)                          |
| Insertion Sort  | O(N<sup>2</sup>)  | O(1)                          |


### Approach 2: Time ComplexityO(N * K)

| Algorithm       | Time Complexity   | Space Complexity (Worst Case) |
|---------------- | ----------------- | ----------------------------- |
| Radix Sort      | O(N * K)          | O(N + K)                      |


### Approach 3: Time Complexity O(N log N)

| Algorithm       | Time Complexity               | Space Complexity (Worst Case) |
|---------------- | ----------------------------- | ----------------------------- |
| Merge Sort      | O(N log N)                    | O(N)                          |
| Quick Sort      | O(N log N) / O(N<sup>2</sup>)  | O(N)                          |
| Heap Sort       | O(N log N)                    | O(1)                          |


### Approach 4: Time Complexity O(N + K)

| Algorithm       | Time Complexity               | Space Complexity (Worst Case) |
|---------------- | ----------------------------- | ----------------------------- |
| Counting Sort   | O(N log N)                    | O(K)                          |
| Bucket Sort     | O(N log N) / O(N<sup>2</sup>) | O(N)                          |


### Approach 4: Optimised

The basic idea that comes to mind is to simply count the number of 0’s, 1’s, and 2’s. Then, place all 0’s at the beginning of the array followed by 1’s and 2's.

| Algorithm       | Time Complexity      | Space Complexity (Worst Case) |
|---------------- | -------------------- | ----------------------------- |
| Brute force     | O(2 * N)             | O(1)                          |

### Approach 5: Efficient approach using single scan: Three-way partitioning

The critical question is: can we solve the problem in a single traversal of the array? We have only three unique elements in the input, so can we use an idea similar to the partition process of the quicksort

We can solve the problem using a single scan by maintaining the correct order of 0’s, 1’s, and 2’s using variables. Actually, we have three types of elements to be placed in sorted order, so we divide the given array into four sections using three-pointers. Let us name these pointers as low, mid, and high.

| Algorithm       | Time Complexity      | Space Complexity (Worst Case) |
|---------------- | -------------------- | ----------------------------- |
| Brute force     | O(N)             | O(1)                          |
