# Approach 1: Brute Force (Using Hashing)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head is None):
            return None
        hasMap = {None: None}
        curr = head
        while(curr):
            hasMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while(curr):
            hasMap[curr].next = hasMap[curr.next]
            hasMap[curr].random = hasMap[curr.random]
            curr = curr.next
        return hasMap[head]

# Time Coplexicity = O(N) = O(N) => Result = Success
# Space Complexity = O(N)
