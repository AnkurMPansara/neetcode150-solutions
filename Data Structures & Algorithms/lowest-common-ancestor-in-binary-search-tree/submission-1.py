# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        data = {None:(False,False)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in data:
                stack.append(node.left)
            elif node.right and node.right not in data:
                stack.append(node.right)
            else:
                node = stack.pop()
                lp, lq = data[node.left]
                rp, rq = data[node.right]
                containP = lp or rp or node.val == p.val
                containQ = lq or rq or node.val == q.val
                if containP and containQ:
                    return node
                data[node] = (containP, containQ)
        return None