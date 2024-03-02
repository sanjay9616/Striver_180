# Approach 2: Two Pointer
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i, j = 0, 0
        l = []
        count = -1
        while (i < n and j < m):
            if (arr1[i] < arr2[j]):
                l.append(arr1[i])
                i += 1
                count += 1
                if (count == k - 1):
                    return l[count]
            elif (arr1[i] == arr2[j]):
                l.append(arr1[i])
                i += 1
                count += 1
                if (count == k - 1):
                    return l[count]
                l.append(arr2[j])
                j += 1
                count += 1
                if (count == k - 1):
                    return l[count]
            else:
                l.append(arr2[j])
                j += 1
                count += 1
                if (count == k - 1):
                    return l[count]
        while (i < n):
            l.append(arr1[i])
            i += 1
            count += 1
            if (count == k - 1):
                return l[count]
        while (j < m):
            l.append(arr2[j])
            j += 1
            if (count == k - 1):
                return l[count]

###################   CLEAR CODE   ##################################
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l = [0] * (n + m)
        inx = 0
        i, j = 0, 0
        while (i < n and j < m):
            if (arr1[i] < arr2[j]):
                l[inx] = arr1[i]
                i += 1
            else:
                l[inx] = arr2[j]
                j += 1
            inx += 1
        while (i < n):
            l[inx] = arr1[i]
            i += 1
            inx += 1
        while (j < m):
            l[inx] = arr2[j]
            j += 1
            inx += 1
        return l[k - 1]


# Time Coplexicity =  O(N + M) => Result = Success
# Space Complexity = O(N + M)
