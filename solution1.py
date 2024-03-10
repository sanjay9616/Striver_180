# Approach 1: Briute Force

def maxMinWindow(arr, n):
    INT_MIN = -maxsize - 1
    INT_MAX = maxsize
    answer = [INT_MIN] * n
    for i in range(n):
        for j in range(i, n):
            start = i
            end = j
            temp = INT_MAX
            for k in range(start, end+1):
                temp = min(temp, arr[k])
            length = end - start
            answer[length] = max(answer[length], temp)
    return answer


# Time Coplexicity = O(N^2 * k) => Result = TLE
# Space Complexity = O(2N)
