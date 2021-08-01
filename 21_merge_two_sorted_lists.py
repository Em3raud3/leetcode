# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def node(list, n):
            if not list:
                return n

            n.next = ListNode(list.pop(0))
            n = n.next
            return node(list, n)

        sorted_list = list()

        while True:
            try:
                sorted_list.append(l1.val)
                l1 = l1.next
            except Exception:
                break

        while True:
            try:
                sorted_list.append(l2.val)
                l2 = l2.next
            except Exception:
                break

        sorted_list.sort()

        if not sorted_list:
            return

        head = ListNode(sorted_list.pop(0))
        current = head

        node(sorted_list, current)

        return(head)
