<h2><a href="https://leetcode.com/problems/pascals-triangle/description/">2. Pascal's Triangle</a></h2>

**In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:.**![Screenshot from 2023-11-19 16-04-39](https://github.com/sanjay9616/Striver_180/assets/87460579/d3664cdc-f096-403e-ba77-b5136b74cc6d)



**Example 1:**

**Input**: numRows = 5

**Output**: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


**Example 2:**

**Input**: numRows = 1

**Output**: [[1]]

**Constraints**:

    • 1 <= numRows <= 30

<h2>Problem 1: </h2>
Find (i<sup>th</sup>, j<sup>th</sup>)

<h2>Solution</h2>
<sup>i-1</sup>C<sub>j-1</sub> = ( i - 2 )! / ( ( j - 1 )! * ( i - j )! )

