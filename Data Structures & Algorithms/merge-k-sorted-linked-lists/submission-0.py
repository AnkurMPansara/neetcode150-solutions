# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(0, None)
        k = len(lists)
        print(f"k: {k}")
        if k == 0:
            return None
        while head:
            minIndex = 0
            for i in range(k):
                if lists[i] and (not lists[minIndex] or lists[i].val < lists[minIndex].val):
                    minIndex = i
            if lists[minIndex]:
                head.next = lists[minIndex]
                head = head.next
                lists[minIndex] = lists[minIndex].next
            else:
                break
        return dummy.next