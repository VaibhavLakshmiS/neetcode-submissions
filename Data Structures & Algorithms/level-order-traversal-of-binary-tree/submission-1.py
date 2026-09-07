# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level = []
            n = len(q)

            for i in range(n):
                curr_node = q.popleft()
                level.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)

                if curr_node.right:
                    q.append(curr_node.right)

            result.append(level)

        return result