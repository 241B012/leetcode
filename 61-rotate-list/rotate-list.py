from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: make circular
        tail.next = head

        # Step 3: reduce k
        k = k % n

        # Step 4: find new tail
        steps = n - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Step 5: new head
        new_head = new_tail.next

        # Step 6: break circle
        new_tail.next = None

        return new_head