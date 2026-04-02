# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return (False, False)
            print(f"Node: {node.val}")
            leftP, leftQ = dfs(node.left)
            rightP, rightQ = dfs(node.right)
            containsP = leftP or rightP or (node.val == p.val)
            containsQ = leftQ or rightQ or (node.val == q.val)
            if containsP and containsQ:
                if not res:
                    res = node
            print(f"P:{containsP} Q:{containsQ}")
            return (containsP, containsQ)
        
        dfs(root)
        return res