# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSwaps(self, values):
        n = len(values)
        min_swaps = 0
        value_to_index = {value: i for i, value in enumerate(values)}

        sorted_values = sorted(values)
        visited = [False] * n

        for i in range(n):
            if visited[i] or value_to_index[sorted_values[i]] == i:
                continue

            # Find the cycle length
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = value_to_index[sorted_values[j]]
                cycle_length += 1

            min_swaps += cycle_length - 1

        return min_swaps
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            curr = []
            for i in range(n):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += self.findSwaps(curr)
        return count

        