# Approach 3: Using Dummy Nodes

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        while(list1 and list2):
            if(list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if(list1):
            curr.next = list1
        if(list2):
            curr.next = list2
        return dummy.next

# Time Coplexicity = O(N + M) => Result = Success
# Space Complexity = O(1)

