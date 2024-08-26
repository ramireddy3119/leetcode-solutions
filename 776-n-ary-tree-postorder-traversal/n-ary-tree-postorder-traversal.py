"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def post(node):
            if not root:
                return 
            for c in node.children:
                post(c)
            res.append(node.val)
        post(root)
        return res

        
        
                