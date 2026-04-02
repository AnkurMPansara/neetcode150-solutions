# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return "null"
            left = dfs(node.left)
            right = dfs(node.right)
            return str(node.val) + left + right
        
        rt = dfs(root)
        srt = dfs(subRoot)
        return srt in rt
        