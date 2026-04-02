# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        depthMap = {None:(0,0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in depthMap:
                stack.append(node.left)
            elif node.right and node.right not in depthMap:
                stack.append(node.right)
            else:
                node = stack.pop()
                ll, lr = depthMap[node.left]
                rl, rr = depthMap[node.right]
                l = 1+max(ll,lr)
                r = 1+max(rl,rr)
                if abs(l-r)>1:
                    return False
                depthMap[node] = (l, r)
        return True
