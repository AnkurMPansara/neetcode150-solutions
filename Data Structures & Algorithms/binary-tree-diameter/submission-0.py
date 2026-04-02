# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = right = middle = 0
        if root.left:
            left = self.diameterOfBinaryTree(root.left)
            middle += self.maxDepth(root.left)
        if root.right:
            right = self.diameterOfBinaryTree(root.right)
            middle += self.maxDepth(root.right)
        print(f"node {root.val} middle:{middle} left:{left} right:{right}")
        return max(middle,max(left,right))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        