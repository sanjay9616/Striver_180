### Approach 1: Brute Force Approach Using Recursion

We can recursively move to right and down from the start until we reach the destination and then add up all valid paths to get the answer.

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(2^N)            | O(N+M)            |

### Approach 2: Memoization  ### Need to Implement

As the above recursive solution has overlapping subproblems so we can declare a 2-D array to save the values for different states of the recursive function and later on use the values of this dp array to get the answer for already solved subproblems


| Algorithm              | Time Complexity          | Space Complexity  |
|----------------------- | ------------------------ | ----------------- |
| Recursion              | O(N * M)                 | O(N * M)         |


### Approach 3: Using DP

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Hashing                |  O(M * N)         | O(M * N)          |

### Approach 4: Using DP (Space Optimization)

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Hashing                |  O(M * N)         | O(N)              |

### Approach 5: Using Combinatorics

Down moves = (m – 1) </br>
Right moves = (n – 1) </br>
Total moves = Down moves + Right moves = (m – 1) + (n – 1) </br>
Choosing positions of (n – 1) ‘R’ characters results in the automatic choosing of (m – 1) ‘D’ character positions </br>

res = <sup>(m + n -2)</sup>C<sub>(n - 1)</sub>

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Hashing                |  O(M)             | O(1)              |
