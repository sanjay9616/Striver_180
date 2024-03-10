# Approach 1: Briute Force

class Solution:
    def myAtoi(self, s: str) -> int:
        multiply, num, flag = 1, 0, 0
        s = s.strip()
        if (len(s) == 0):
            return 0
        if (s[0] == "-"):
            multiply = -1
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
                flag = 1
            elif (i == "+" or i == "-") and (flag == 0):
                flag = 1
            else:
                break
        num = num * multiply
        if (-2**31 <= num <= (2**31)-1):
            return num
        elif (num < 0):
            return -2**31
        else:
            return 2**31-1

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
