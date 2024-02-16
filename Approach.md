### Approach 1: Brute Force (we use O(n) extra space for vector to store the linked list values and we simply return middle value of vector)

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N)              | O(N)              |


### Approach 2: Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2.

| Algorithm                    | Time Complexity   | Space Complexity  |
|----------------------------- | ----------------- | ----------------- |
| Brute Force(Space Optimized) | O(N)              | O(1)              |

### Approach 3: Traverse linked list using two-pointers. Move one pointer by one and the other pointers by two. When the fast pointer reaches the end, the slow pointer will reach the middle of the linked list.

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Two Pointer            | O(N)              | O(1)              |
