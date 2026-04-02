# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        head = dummy
        while head:
            old = head
            start = head.next
            i = 0
            while i < k and head:
                head = head.next
                i += 1
            if head:
                old.next = head
                end = head.next
                head = start
                for j in range(k):
                    tmp = start
                    start = start.next
                    tmp.next = end
                    end = tmp
                    print(f"end{end.val}")
        return dummy.next