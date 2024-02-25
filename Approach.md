### Approach 1: Brute Force
Traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and the height of the current element is the amount of water that can be stored in this array element.


| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N^2)            | O(1)              |


### Approach 2: Precalculation
In previous approach, for every element we needed to calculate the highest element on the left and on the right using prefix and suffix.

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Precalculation         | O(N)              | O(N)              |

### Approach 3: Using Stack  ## NEED TO IMPLEMENT

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Using Stack            | O(N)              | O(N)              |

### Approach 4: Horizontal Scan Method

| Algorithm              | Time Complexity        | Space Complexity  |
|----------------------- | ---------------------- | ----------------- |
| Horizontal Scan Method | O(max (max_height, N)) | O(1)              |

### Approach 5: Two Pointer ## Need To Revised

| Algorithm              | Time Complexity        | Space Complexity  |
|----------------------- | ---------------------- | ----------------- |
| Two Pointer            | O(N)                   | O(1)              |

### Approach 6: Similar to Linear Search    ### NEED TO IMPLEMENT

| Algorithm                | Time Complexity        | Space Complexity  |
|-------------------=----- | ---------------------- | ----------------- |
|Similar to Linear Search  | O(N)                   | O(1)              |

