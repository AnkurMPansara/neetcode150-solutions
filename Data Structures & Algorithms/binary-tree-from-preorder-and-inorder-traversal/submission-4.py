# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preHead = inHead = 0
        def dfs(limit):
            nonlocal preHead, inHead
            print(f"\npreHead:{preHead} inHead:{inHead} limit:{limit}")
            if preHead >= len(preorder):
                return None
            if inorder[inHead] == limit:
                inHead += 1
                return None

            node = TreeNode(preorder[preHead])
            print(f"Made node:{node.val}")
            preHead += 1
            print(f"Invoked left of {node.val}")
            node.left = dfs(node.val)
            print(f"Invoked right of {node.val}")
            node.right = dfs(limit)
            return node
        return dfs(1001)