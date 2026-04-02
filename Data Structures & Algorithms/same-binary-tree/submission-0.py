# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            l = dfs(node1.left, node2.left)
            r = dfs(node1.right, node2.right)
            if l and r and node1.val == node2.val:
                return True
            return False
        
        return dfs(p, q)