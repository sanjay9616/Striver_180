# Need to Revise
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getGroupEnd(cur, k):
            while k > 1 and cur.next:
                cur = cur.next
                k -= 1
            return cur if k == 1 else None

        def reverseGroup(start, end):
            prev, cur, new_group_start = None, start, end.next
            while cur != new_group_start:
                cur.next, cur, prev = prev, cur.next, cur
        dummy = ListNode()
        prev_group = dummy
        while head:
            group_start = head
            group_end = getGroupEnd(head, k)
            if not group_end:
                break
            next_group_start = group_end.next
            reverseGroup(group_start, group_end)
            prev_group.next = group_end
            prev_group = group_start
            group_start.next = next_group_start
            head = next_group_start
        return dummy.next
