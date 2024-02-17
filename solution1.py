# Approach 1: Brute Force

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodeValue = []
        curr1, curr2 = list1, list2
        while(curr1):
            nodeValue.append(curr1.val)
            curr1 = curr1.next
        while(curr2):
            nodeValue.append(curr2.val)
            curr2 = curr2.next
        nodeValue.sort()
        newList = curr = ListNode(-1)
        for i in nodeValue:
            curr.next = ListNode(i)
            curr = curr.next
        return newList.next


# Time Coplexicity = O(N + M) + O(N + M) + O((N + M) * log(N + M)) = O((N + M) * log(N + M) => Result = Success
# Space Complexity = O(N + M)
