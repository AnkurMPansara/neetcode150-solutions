# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        head = dummy
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            head.next = ListNode(s%10, None)
            carry = s//10
            head, l1, l2 = head.next, l1.next, l2.next
        while l1:
            s = l1.val + carry
            head.next = ListNode(s%10, None)
            carry = s//10
            head, l1 = head.next, l1.next
        while l2:
            s = l2.val + carry
            head.next = ListNode(s%10, None)
            carry = s//10
            head, l2 = head.next, l2.next
        if carry>0:
            head.next = ListNode(carry, None)
        return dummy.next