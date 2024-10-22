# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return -1
        queue = deque([root])
        arr = []
        while queue:
            n = len(queue)
            levelSum = 0
            for _ in range(n):
                current = queue.popleft()
                levelSum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            arr.append(levelSum)
        if k > len(arr):
            return -1
        arr.sort()
        return arr[-k]
        