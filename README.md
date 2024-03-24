<h2><a href="https://leetcode.com/problems/edit-distance/description/">154. Edit Distance</a></h2>

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

1. Insert a character </br>
2. Delete a character </br>
3. Replace a character </br>

**Example 1**:

**Input**: word1 = "horse", word2 = "ros"

**Output**: 3

**Explanation**: </br>
horse -> rorse (replace 'h' with 'r') </br>
rorse -> rose (remove 'r') </br>
rose -> ros (remove 'e') </br>

**Example 2**:

**Input**: word1 = "intention", word2 = "execution"

**Output**: 5

**Explanation**: </br>
intention -> inention (remove 't') </br>
inention -> enention (replace 'i' with 'e') </br>
enention -> exention (replace 'n' with 'x') </br>
exention -> exection (replace 'n' with 'c') </br>
exection -> execution (insert 'u') </br>



**Constraints**:

    • 0 <= word1.length, word2.length <= 500
    • word1 and word2 consist of lowercase English letters.