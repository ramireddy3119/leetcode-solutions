# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hashSet = set()
        root.val = 0
        self.hashSet.add(0)
        def dfs(root,val):
            if not root:
                return
            self.hashSet.add(val)
            dfs(root.left,2*val+1)
            dfs(root.right,2*val+2)
            
        dfs(root.left,1)
        dfs(root.right,2)
    def find(self, target: int) -> bool:
        return True if target in self.hashSet else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)