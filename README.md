<h2><a href="https://leetcode.com/problems/min-stack/description/">83. Min Stack</a></h2>

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

1. MinStack() initializes the stack object. </br>
2. void push(int val) pushes the element val onto the stack. </br>
3. void pop() removes the element on the top of the stack. </br>
4. int top() gets the top element of the stack. </br>
5. int getMin() retrieves the minimum element in the stack. </br>

You must implement a solution with O(1) time complexity for each function.

**Example 1**:

**Input**: ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]

**Output**: [null,null,null,null,-3,null,0,-2]

**Explanation**:

MinStack minStack = new MinStack(); </br>
minStack.push(-2);</br>
minStack.push(0);</br>
minStack.push(-3);</br>
minStack.getMin(); // return -3</br>
minStack.pop();</br>
minStack.top();    // return 0</br>
minStack.getMin(); // return -2</br>


**Constraints**:

    • -2^31 <= val <= 2^31 - 1
    • Methods pop, top and getMin operations will always be called on non-empty stacks.
    • At most 3 * 10^4 calls will be made to push, pop, top, and getMin.