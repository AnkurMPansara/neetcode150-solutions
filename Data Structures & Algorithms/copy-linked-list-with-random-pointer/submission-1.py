"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ptr1, ptr2 = head, Node(head.val, None, None)
        headCopy = ptr2
        nodeMap = {ptr1:ptr2}
        while ptr1.next:
            ptr1 = ptr1.next
            ptr2.next = Node(ptr1.val, None, None)
            ptr2 = ptr2.next
            nodeMap[ptr1] = ptr2
        ptr1 = head
        ptr2 = headCopy
        while ptr1:
            if ptr1.random:
                print(f"ptr1 {ptr1.val} has random value of {ptr1.random.val}")
                ptr2.random = nodeMap[ptr1.random]
                print(f"ptr2 {ptr2.val} is assigned random value of {ptr2.random.val}")
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return headCopy
        

        