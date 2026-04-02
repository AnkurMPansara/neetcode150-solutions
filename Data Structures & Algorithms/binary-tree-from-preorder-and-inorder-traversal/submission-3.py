# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookupIn = {val: idx for idx, val in enumerate(inorder)}
        preHead = 0
        def dfs(l, r):
            nonlocal preHead

            if l > r:
                return None
            val = preorder[preHead]
            preHead += 1
            node = TreeNode(val)
            mid = lookupIn[val]
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node
        
        return dfs(0, len(preorder)-1)