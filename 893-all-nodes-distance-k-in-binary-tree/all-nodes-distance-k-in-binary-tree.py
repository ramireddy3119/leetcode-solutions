# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def markParents(root, parent_track, target):
            queue = deque([root])
            while queue:
                current = queue.popleft()
                if current.left:
                    parent_track[current.left] = current
                    queue.append(current.left)
                if current.right:
                    parent_track[current.right] = current
                    queue.append(current.right)

        parent_track = {}
        markParents(root, parent_track, target)
        
        visited = {}
        queue = deque([target])
        visited[target] = True
        curr_level = 0
        
        while queue:
            size = len(queue)
            if curr_level == k:
                break
            curr_level += 1

            for i in range(size):
                current = queue.popleft()
                
                if current.left and current.left not in visited:
                    queue.append(current.left)
                    visited[current.left] = True
                
                if current.right and current.right not in visited:
                    queue.append(current.right)
                    visited[current.right] = True
                
                if current in parent_track and parent_track[current] not in visited:
                    queue.append(parent_track[current])
                    visited[parent_track[current]] = True

        result = [node.val for node in queue]
        return result
        