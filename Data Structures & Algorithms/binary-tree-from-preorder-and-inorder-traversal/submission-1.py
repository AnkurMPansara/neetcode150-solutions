# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookupPre = {preorder[i]:i for i in range(len(preorder))}
        lookupIn = {inorder[i]:i for i in range(len(inorder))}
        brokentrees = []
        nodeMap = {val:TreeNode(val, None, None) for val in preorder}
        for i in range(len(preorder)-1):
            cur, nxt = preorder[i], preorder[i+1]
            if lookupIn[cur] > lookupIn[nxt]:
                nodeMap[cur].left = nodeMap[nxt]
            else:
                brokentrees.append(nxt)
        for elem in brokentrees:
            i = lookupIn[elem] - 1
            while lookupPre[inorder[i]] > lookupPre[elem]:
                i -= 1
            print(f"head:{elem} parent:{inorder[i]}")
            nodeMap[inorder[i]].right = nodeMap[elem]
        return nodeMap[preorder[0]]