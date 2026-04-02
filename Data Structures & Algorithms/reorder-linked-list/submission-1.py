# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        if n < 3:
            return
        midpoint = n//2 if n%2==0 else n//2+1
        print(f"mid: {midpoint}")
        second_part = head
        i = 0
        while i<midpoint:
            i += 1
            second_part = second_part.next
        print(f"second part: {second_part.val}")
        curr, prev = second_part, None
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        curr = prev
        print(f"reversed: {prev.val}")
        dummy = ListNode(0)
        ans = dummy
        while curr:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = curr
            curr = curr.next
            dummy = dummy.next
        dummy.next = head
        dummy = dummy.next
        if dummy:
            dummy.next = None
        head = ans.next
        return