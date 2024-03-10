# Approach 1: Briute Force (Roman to Integer)

class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s=s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        res = 0
        for i in s:
            res += hashMap[i]
        return res


# Approach 1: Briute Force (Integer to Roman)
class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {1: "I", 5: "V", 4: "IV", 10: "X", 9: "IX", 50: "L", 40: "XL", 100: "C", 90: "XC", 500: "D",  400: "CD", 1000: "M", 900: "CM"}
        res = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while(n <= num):
                res += num_map[n]
                num -= n
        return res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
