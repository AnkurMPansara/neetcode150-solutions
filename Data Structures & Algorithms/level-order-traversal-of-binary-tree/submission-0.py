# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,1)])
        traversal = []
        while queue:
            node, level = queue.popleft()
            if len(traversal) < level:
                traversal.append([node.val])
            else:
                traversal[-1].append(node.val)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right, level+1))
        return traversal
        