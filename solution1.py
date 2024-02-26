# Approach 1: Greedy approach

def maximumMeetings(self, n, start, end):
    ans, l = [], []
    for i in range(n):
        l.append([start[i], end[i]])
    l.sort(key=lambda x: x[1])
    ans.append(l[0])
    for i in range(1, n):
        if l[i][0] > ans[-1][1]:
            ans.append(l[i])
    return len(ans)

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
