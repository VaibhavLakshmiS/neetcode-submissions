class Solution:
    def Preorder(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.Preorder(root.left)
        right_depth = self.Preorder(root.right)

        return 1 + max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.Preorder(root)