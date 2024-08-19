# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfsHeight(self,root):
            if root is None:
                return 0
        
            LH = dfsHeight(self,root.left)
            if LH == -1: return -1

            RH = dfsHeight(self,root.right)
            if RH == -1: return -1

            if abs(LH-RH) > 1: return -1

            return max(LH,RH)+1
        
        return dfsHeight(self,root) != -1
        