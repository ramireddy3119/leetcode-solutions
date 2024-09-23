# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def helper(root):
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightChild = root.right
                lastRight = findLastRight(root.left)
                lastRight.right = rightChild
                return root.left
        def findLastRight(root):
            if root.right == None:
                return root
            return findLastRight(root.right)
        if root.val == key:
            return helper(root)
        
        dummy = root
        while root:
            if root.val > key:
                if root.left  and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right  and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right
        return dummy

        def helper(root):
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightChild = root.right
                lastRight = findLastRight(root.left)
                return root.left
        def findLastRight(root):
            if root.right == None:
                return root
            self.findLastRight(root.right)