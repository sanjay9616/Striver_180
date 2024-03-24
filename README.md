<h2><a href="https://www.codingninjas.com/studio/problems/1072980?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website">153. 0 1 Knapsack</a></h2>

A thief is robbing a store and can carry a maximum weight of ‘W’ into his knapsack. There are 'N' items available in the store and the weight and value of each item is known to the thief. Considering the constraints of the maximum weight that a knapsack can carry, you have to find the maximum profit that a thief can generate by stealing items.

Note: The thief is not allowed to break the items.

For example, N = 4, W = 10 and the weights and values of items are weights = [6, 1, 5, 3] and values = [3, 6, 1, 4]. Then the best way to fill the knapsack is to choose items with weight 6, 1 and 3. The total value of knapsack = 3 + 6 + 4 = 13.



**Example 1**:

**Input**: </br>
1 </br>
4 5 </br>
1 2 4 5 </br>
5 4 8 6 </br>

**Output**: 13

**Explanation**: The most optimal way to fill the knapsack is to choose items with weight 4 and value 8, weight 1 and value 5.

The total value of the knapsack =  8 + 5 = 13.

**Example 2**:

**Input**: </br>
1 </br>
5 100 </br>
20 24 36 40 42 </br>
12 35 41 25 32 </br>

**Output**: 101


**Constraints**:

    • 1 <= T <= 10
    • 1 <= N <= 10^3
    • 1 <= W <= 10^3
    • 1<= weights <=10^3
    • 1 <= values <= 10^3