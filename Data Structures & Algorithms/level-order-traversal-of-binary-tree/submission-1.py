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
        res = []
        stack = [(root, 0)]
        visited = set()
        while stack:
            node, level = stack[-1]
            if len(res) == level:
                res.append([])
            if node.left and node.left not in visited:
                stack.append((node.left, level+1))
            elif node.right and node.right not in visited:
                stack.append((node.right, level+1))
            else:
                node, level = stack.pop()
                res[level].append(node.val)
                visited.add(node)
        return res
        