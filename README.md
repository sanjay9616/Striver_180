<h2><a href="https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website">77. Sort a Stack</a></h2>

You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.

We can only use the following functions on this stack S.

is_empty(S) : Tests whether stack is empty or not. </br>
push(S) : Adds a new element to the stack. </br>
pop(S) : Removes top element from the stack. </br>
top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.</br>

**Note** :

1) Use of any loop constructs like while, for..etc is not allowed. </br>
2) The stack may contain duplicate integers. </br>
3) The stack may contain any integer i.e it may either be negative, positive or zero. </br>

**Example 1**:

**Input** nums1 = [5, -2, 9, -7, 3]

**Output**: [9, 5, 3, -2, -7]

**Explanation**: 9 Is the largest element, hence it’s present at the top. Similarly 5>3, 3>-2 and -7 being the smallest element is present at the last.

**Example 2**:

**Input** nums1 = [-3, 14, 18, -5, 30]

**Output**: [30, 18, 14, -3, -5]

**Explanation**: 30 is the largest element, hence it’s present at the top. Similarly, 18>14, 14>-3 and -5 being the smallest element is present at the last.

**Constraints**:

    • 1 <= 'T' <= 100
    • 1 <=  'N' <= 100
    • 1 <= |'V'| <= 10^9, Where |V| denotes the absolute value of any stack element.
    • Time limit: 1 sec