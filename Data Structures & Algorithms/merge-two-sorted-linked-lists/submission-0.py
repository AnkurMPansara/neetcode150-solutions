# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        ans = ListNode(-101)
        head = ans
        while head1 and head2:
            if head1.val < head2.val:
                temp = head1
                head1 = head1.next
                temp.next = None
                ans.next = temp
                ans = ans.next
            else:
                temp = head2
                head2 = head2.next
                temp.next = None
                ans.next = temp
                ans = ans.next
        if head1:
            ans.next = head1
        else:
            ans.next = head2
        return head.next