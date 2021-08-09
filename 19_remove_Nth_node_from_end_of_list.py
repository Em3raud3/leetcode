# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        if length == n:
            return head.next

        t = length - n

        current = head
        while t > 1:
            current = current.next
            t -= 1

        try:
            current.next = current.next.next
        except Exception:
            current.next = None

        return head

# ? class Solution:
# ?     def removeNthFromEnd(self, head, n):
# ?         fast = slow = head
# ?         for _ in range(n):
# ?             fast = fast.next
# ?         if not fast:
# ?             return head.next
# ?         while fast.next:
# ?             fast = fast.next
# ?             slow = slow.next
# ?         slow.next = slow.next.next
# ?         return head
