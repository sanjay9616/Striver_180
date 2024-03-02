<h2><a href="https://www.codingninjas.com/studio/problems/median-of-a-row-wise-sorted-matrix_1115473?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf">60. Median in a row-wise sorted Matrix</a></h2>

You are given a row-wise sorted matrix 'mat' of size m x n where 'm' and 'n' are the numbers of rows and columns of the matrix, respectively.

Your task is to find and return the median of the matrix.

**Note**: 'm' and 'n' will always be odd.


**Example**: Input: 'n' = 5, 'm' = 5, 'mat' = [[ 1, 5, 7, 9, 11 ], [ 2, 3, 4, 8, 9 ],[ 4, 11, 14, 19, 20 ],[ 6, 10, 22, 99, 100 ],[ 7, 15, 17, 24, 28 ]]

**Output**: 10

**Explanation**: If we arrange the elements of the matrix in the sorted order in an array, they will be like this-</br>
1 2 3 4 4 5 6 7 7 8 9 9 10 11 11 14 15 17 19 20 22 24 28 99 100 </br>
So the median is 10, which is at index 12, which is midway as the total elements are 25, so the 12th index is exactly midway. Therefore, the answer will be 10. </br>

**Sample Input 1**: </br>
5 5 </br>
1 5 7 9 11 </br>
2 3 4 8 9 </br>
4 11 14 19 20 </br>
6 10 22 99 100 </br>
7 15 17 24 28 </br>

**Sample Output 1**: 10

**Explanation For Sample Input 1**: If we arrange the elements of the matrix in the sorted order in an array, they will be like this- </br>
1 2 3 4 4 5 6 7 7 8 9 9 10 11 11 14 15 17 19 20 22 24 28 99 100 </br>
So the median is 10, which is at index 12, which is midway as the total elements are 25, so the 12th index is exactly midway. Therefore, the answer will be 10. 

**Sample Input 2**: </br>
3 5 </br>
1 2 3 4 5 </br>
8 9 11 12 13 </br>
21 23 25 27 29 </br>

**Sample Output 2**: 11

**Explanation For Sample Input 2**: If we arrange the elements of the matrix in the sorted order in an array, they will be like this- </br>
1 2 3 4 5 8 9 11 12 13 21 23 25 27 29 </br>
So the median is 11, which is at index 7, which is midway as the total elements are 15, so the 7th index is exactly midway. Therefore, the answer will be 11. </br>

**Expected Time Complexity**: Try to solve this in O(32 * m * log(n)).

**Constraints**:

    • 1 <= m < 100
    • 1 <= n < 100
    • 1 <= mat[i][j] <=10^9
    • Time Limit: 1 sec
