### Approach 1: Brute Froce
The idea is to take every interval one by one and find the number of intervals that overlap with it</br>
Arrival time of 1st train is greater then or equal to 2nd tain and departure time of 2nd train is greater then or equal to fiest train.


| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N^2)            | O(1)              |

### Approach 2: Using Heap
Store the arrival time and departure time and sort them based on arrival time then check if the arrival time of the next train is smaller than the departure time of the previous train if it is smaller then increment the number of the platforms needed otherwise not.


| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N*log(N))       | O(N)              |

### Approach 3: Using Sorting  ## Need to Implement

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N*log(N))       | O(1)              |

### Approach 4: Using Sweep Line Algorithm

| Algorithm              | Time Complexity   | Space Complexity      |
|----------------------- | ----------------- | --------------------- |
| Brute Force            | O(N)              | O(N)                  |



