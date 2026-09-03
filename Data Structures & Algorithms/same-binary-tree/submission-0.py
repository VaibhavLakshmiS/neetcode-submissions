# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        def dfs(p,q):
            if (not p and q) or (p and not q):
                self.same = False
                return
            if not p and not q:
                return
            dfs(p.left,q.left)
            dfs(p.right,q.right)
            if p.val != q.val:
                self.same = False
        dfs(p,q)
        return self.same
            

        