<h2><a href="https://www.codingninjas.com/studio/problems/max-of-min_982935?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website">86. Maximum of minimum for every window size</a></h2>

You are given an array of ‘N’ integers, you need to find the maximum of minimum for every window size. The size of the window should vary from 1 to ‘N’ only.

For example:

ARR = [1,2,3,4] </br>
Minimums of window size 1 = min(1), min(2), min(3), min(4) = 1,2,3,4 </br>
Maximum among (1,2,3,4)  is 4 </br>

Minimums of window size 2 = min(1,2), min(2,3),   min(3,4) = 1,2,3 </br>
Maximum among (1,2,3) is 3 </br>

Minimums of window size 3 = min(1,2,3), min(2,3,4) = 1,2 </br>
Maximum among (1,2) is 2 </br>

Minimums of window size 4 = min(1,2,3,4) = 1 </br>
Maximum among them is 1 </br>
The output array should be [4,3,2,1]. </br>

**Example 1**:

**Input**: </br>
2 </br>
4 </br>
1 2 3 4 </br>
5 </br>
3 3 4 2 4  </br>

**Output**: </br>
4 3 2 1 </br>
4 3 3 2 2 </br>

**Example 2**:

**Input**: </br>
2 </br>
5 </br>
45 -2 42 5 -11  </br>
6 </br>
-2 12 -1 1 20 1   </br>

**Output**: </br>
45 5 -2 -2 -11 </br>
20 1  1 -1 -1 -2 </br>


**Constraints**:

    • 1 <= T <= 100
    • 1 <= N <= 10 ^ 4 
    • -10 ^ 9 <= ARR[i] <= 10 ^ 9
    • Where ‘T’ is the number of test cases, ‘N’ is the size of the array and ‘ARR[i]’ is the size of the array elements.
    • Time Limit: 1 sec
