<h2><a href="https://www.interviewbit.com/problems/allocate-books/">65. Allocate Books</a></h2>

Given an array of integers A of size N and an integer B.

The College library has N books. The ith book has A[i] number of pages.

You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

1. A book will be allocated to exactly one student. </br>
2. Each student has to be allocated at least one book. </br>
3. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2. </br>

Calculate and return that minimum possible number.

**NOTE**: Return -1 if a valid assignment is not possible.

**Example 1**:

**Input**:A = [12, 34, 67, 90], B = 2

**Output**: 113

**Explanation**: There are two students. Books can be distributed in following fashion : </br>
1. [12] and [34, 67, 90] Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages </br>
2. [12, 34] and [67, 90] Max number of pages is allocated to student 2 with 67 + 90 = 157 pages </br>
3. [12, 34, 67] and [90] Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages Of the 3 cases, Option 3 has the minimum pages = 113.


**Example 2**:

**Input**: A = [5, 17, 100, 11], B = 4

**Output**: 100

**Constraints**:

    • 1 <= N <= 105
    •  1 <= A[i], B <= 105