# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_val):
            if not node:
                return 0
            res = 0
            if node.val>=max_val:
                res = 1
            max_val = max(node.val,max_val)
            res+=dfs(node.left,max_val)
            res+=dfs(node.right,max_val)
            return res
        return dfs(root,root.val)
            


        