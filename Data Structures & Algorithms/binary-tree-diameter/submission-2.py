# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        stack = [root]
        data = {None: (0,0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in data:
                stack.append(node.left)
            elif node.right and node.right not in data:
                stack.append(node.right)
            else:
                node = stack.pop()

                depthL, diamL = data[node.left]
                depthR, diamR = data[node.right]
                data[node] = (1+max(depthL, depthR), max(depthL+depthR, diamL, diamR))
        
        return data[root][1]
      