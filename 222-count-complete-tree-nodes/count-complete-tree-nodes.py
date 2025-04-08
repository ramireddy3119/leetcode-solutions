# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def preorder(root):
            if not root:
                return
            count[0] += 1
            preorder(root.left)
            preorder(root.right)
        count = [0]
        preorder(root)
        return count[0]
        