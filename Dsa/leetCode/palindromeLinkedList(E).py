from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode])->bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # At this point, `prev` is the head of the reversed second half
        # and `head` is the head of the first half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True