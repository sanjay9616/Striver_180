# Approach 1: Brute Force

def immediateSmaller(a: List[int]) -> None:
    for i in range(len(a) - 1):
        if(a[i + 1] < a[i]):
            a[i] = a[i + 1]
        else:
            a[i] = -1
    a[-1] = -1

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)