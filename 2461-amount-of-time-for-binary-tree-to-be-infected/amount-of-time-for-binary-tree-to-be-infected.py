from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = dict()
        target = self.markParent(root, start, parent)
        
        queue = deque([target])
        vis = set([target])
        time = 0
        
        while queue:
            n = len(queue)
            burned = False
            for _ in range(n):
                node = queue.popleft()
                for nei in [node.left, node.right, parent.get(node)]:
                    if nei and nei not in vis:
                        queue.append(nei)
                        vis.add(nei)
                        burned = True
            if burned:
                time += 1
        return time

    def markParent(self, root, start, parent):
        queue = deque([root])
        target = None
        while queue:
            node = queue.popleft()
            if node.val == start:
                target = node
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        return target
