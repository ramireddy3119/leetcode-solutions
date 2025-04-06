# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fun(root,p,q):
            if not root:
                return None
            if p.val > root.val and q.val > root.val:
                return fun(root.right,p,q)
            elif p.val < root.val and q.val < root.val:
                return fun(root.left,p,q)
            return root
        return fun(root,p,q)
        