# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root,0,res)
        return res
    
    def recursion(self,node,level,res):
            if not node:
                return 
            
            if len(res) == level:
                res.append(node.val)
            self.recursion(node.right,level+1,res)
            self.recursion(node.left,level+1,res)
        
        