# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycler = ListNode(0)
        while head:
            if head.next == cycler:
                return True
            else:
                tmp = head
                head = head.next
                tmp.next = cycler
        return False