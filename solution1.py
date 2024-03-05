# Approach 1: Using Stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (len(stack) > 0 and (
                (i == ')' and stack[-1] == '(') or
                (i == '}' and stack[-1] == '{') or
                (i == ']' and stack[-1] == '[')
            )):
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
