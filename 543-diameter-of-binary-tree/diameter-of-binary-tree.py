# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findMax(self,root,maxi):
            if root is None:
                return 0
            LH = findMax(self,root.left,maxi)
            RH = findMax(self,root.right,maxi)
            maxi[0] = max(maxi[0],LH+RH)
            return 1+max(LH,RH)
        maxi = [0]
        findMax(self,root,maxi)
        return maxi[0]

