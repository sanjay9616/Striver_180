# Approach 1: Linear Search

def NthRoot(n: int, m: int) -> int:
    for i in range(m, 0, -1):
        if(i ** n == m):
            return i
    return -1

# Time Coplexicity = O(M * log(N)) => Result = TLE
# Space Complexity = O(1)



# Approach 1: Linear Search (similar to above but optimized)

def NthRoot(n: int, m: int) -> int:
    for i in range(1, m+1):
        if(i ** n == m):
            return i
        elif(i ** n > m):
            return -1
    return -1

# Time Coplexicity = < O(M * log(N)) => Result = Success
# Space Complexity = O(1)
