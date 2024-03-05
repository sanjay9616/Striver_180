<h2><a href="https://leetcode.com/problems/valid-parentheses/description/">75. Valid Parentheses</a></h2>

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if: </br>
1. Open brackets must be closed by the same type of brackets. </br>
2. Open brackets must be closed in the correct order. </br>
3. Every close bracket has a corresponding open bracket of the same type. </br>

**Example 1**:

**Input** s = "()"

**Output**: true

**Example 1**:

**Input** s = "()[]{}"

**Output**: true

**Example 1**:

**Input** s = "(]"

**Output**: false


**Constraints**:

    • 1 <= s.length <= 10^4
    • s consists of parentheses only '()[]{}'