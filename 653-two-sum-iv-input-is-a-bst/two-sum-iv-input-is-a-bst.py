class BSTIterator:
    def __init__(self, root, reverse=False):
        self.stack = []
        self.reverse = reverse
        self._push_nodes(root)

    def _push_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left  

    def next(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        self._push_nodes(node.left if self.reverse else node.right)
        return node.val

    def has_next(self):
        return len(self.stack) > 0


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        left_iter = BSTIterator(root, reverse=False)  # Smallest values first
        right_iter = BSTIterator(root, reverse=True)  # Largest values first

        left_val = left_iter.next()
        right_val = right_iter.next()

        while left_val is not None and right_val is not None and left_val < right_val:
            current_sum = left_val + right_val
            if current_sum == k:
                return True
            elif current_sum < k:
                left_val = left_iter.next()  # Move left iterator forward
            else:
                right_val = right_iter.next()  # Move right iterator backward

        return False
