class Solution:
    def Post(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.Post(root.left)
        self.Post(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.Post(root)
        return root