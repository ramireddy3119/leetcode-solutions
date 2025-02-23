class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        def build(preorder, postorder):
            if not preorder or not postorder:
                return None

            root = TreeNode(preorder[0])

            if len(preorder) == 1:
                return root

            left_subtree_root_val = preorder[1]
            left_subtree_size = postorder.index(left_subtree_root_val) + 1

            root.left = build(preorder[1:1+left_subtree_size], postorder[:left_subtree_size])
            root.right = build(preorder[1+left_subtree_size:], postorder[left_subtree_size:-1])

            return root

        return build(preorder, postorder)