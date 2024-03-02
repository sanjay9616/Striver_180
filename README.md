<h2><a href="https://www.codingninjas.com/studio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website">59. Find Nth Root Of M</a></h2>

You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. If the 'nth root is not an integer, return -1.

**Note**: 'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


**Example**: Input: ‘n’ = 3, ‘m’ = 27

**Output**: 3

**Explanation**: 3rd Root of 27 is 3, as (3)^3 equals 27.

**Sample Input 1**: 3 27

**Sample Output 1**: 3

**Explanation For Sample Input 1**: 3rd Root of 27 is 3, as (3)^3 equals 27.

**Sample Input 2**: 4 69

**Sample Output 2**: -1

**Explanation For Sample Input 2**: 4th Root of 69 is not an integer, hence -1.

**Expected Time Complexity**: Try to do this in O(log(n+m)).

**Constraints**:

1 <= n <= 30
1 <= m <= 10^9
Time Limit: 1 sec.