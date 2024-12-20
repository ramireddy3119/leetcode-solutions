# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            curr_level = []
            for _ in range(n):
                node = queue.popleft()
                curr_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                n = len(curr_level)
                for i in range(n//2):
                    curr_level[i].val,curr_level[n-i-1].val = curr_level[n-i-1].val,curr_level[i].val
            level += 1
        return root

        