# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        if not l1 and not l2:
            return l1

        digits = list()

        while l1 or l2:
            x = 0

            if l1:
                x += l1.val
                l1 = l1.next

            if l2:
                x += l2.val
                l2 = l2.next

            digits.append(x)

        # * This portion is similar to easy 66. plus one exercise
        for i in range(len(digits)):
            if digits[i] >= 10:

                a = digits[i] % 10
                b = digits[i]//10
                digits[i] = a

                if i == len(digits) - 1:
                    digits.append(b)

                else:
                    digits[i+1] = digits[i+1] + b

        if digits:
            head = ListNode(digits.pop(0))

        current = head

        while digits:
            current.next = ListNode(digits.pop(0))
            current = current.next

        return head
