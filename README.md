<h2><a href="https://leetcode.com/problems/roman-to-integer/description/">91. String to Integer (atoi) / STRSTR</a></h2>


Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace. </br>

2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present </br>

3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored. </br>

4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2). </br>

5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1. </br>

6. Return the integer as the final result. </br>

**Note**:

1. Only the space character ' ' is considered a whitespace character. </br>
2. Do not ignore any characters other than the leading whitespace or the rest of the string after the digits. </br>



**Example 1:**

**Input**: s = "42"

**Output**: 42

**Explanation**:

The underlined characters are what is read in, the caret is the current reader position. </br>
Step 1: "42" (no characters read because there is no leading whitespace) </br>
Step 2: "42" (no characters read because there is neither a '-' nor '+') </br>
Step 3: "42" ("42" is read in) </br>
The parsed integer is 42. </br>
Since 42 is in the range [-231, 231 - 1], the final result is 42. </br>

**Example 2:**

**Input**: s = "   -42"

**Output**: -42

**Explanation**:

Step 1: "   -42" (leading whitespace is read and ignored) </br>
Step 2: "   -42" ('-' is read, so the result should be negative) </br>
Step 3: "   -42" ("42" is read in)
The parsed integer is -42. </br>
Since -42 is in the range [-231, 231 - 1], the final result is -42. </br>

**Example 2:**

**Input**: s = "4193 with words"

**Output**: 4193

**Explanation**:

Step 1: "4193 with words" (no characters read because there is no leading whitespace) </br>
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+') </br>
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit) </br>
The parsed integer is 4193. </br>
Since 4193 is in the range [-231, 231 - 1], the final result is 4193. </br>


**Constraints**:

    • 0 <= s.length <= 200
    • s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.