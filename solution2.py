# Approach 1: Binary Search

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        if(m == power):
            return mid
        elif(m > power):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Time Coplexicity = < O(log(N)) => Result = Success
# Space Complexity = O(1)