# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self,node: Optional[TreeNode], subRoot: Optional[TreeNode]):
        self.same = True
        def dfs(node,subRoot):
            if (not node and subRoot) or (node and not subRoot):
                self.same = False
                return 
            if (not node and not subRoot):
                return 
            dfs(node.left,subRoot.left)
            dfs(node.right,subRoot.right)
            if node.val != subRoot.val:
                self.same = False
        dfs(node,subRoot)
        return self.same

 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or  self.isSubtree(root.right,subRoot))

