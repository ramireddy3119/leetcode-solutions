# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def isFound(root):
            if not root:
                return False
            rem = k - root.val
            if rem in seen:
                return True
            seen.add(root.val)
            return isFound(root.right) or isFound(root.left)
        seen = set()
        return isFound(root)