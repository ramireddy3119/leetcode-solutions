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
        def dfs(root):
            if not root:
                return 
            if root.left:
                self.hashSet.add(root.val * 2 + 1)
                root.left.val = root.val * 2 + 1
                dfs(root.left)
            if root.right:
                self.hashSet.add(root.val * 2 + 2)
                root.right.val = root.val * 2 + 2
                dfs(root.right)
        dfs(root)
    def find(self, target: int) -> bool:
        return True if target in self.hashSet else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)