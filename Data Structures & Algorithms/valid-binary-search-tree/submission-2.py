# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root, res) -> list[int]:
        if not root:
            return
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = self.inOrder(root, [])

        max_val = float('-inf')
        for num in res:
            if num <= max_val:
                return False
            max_val = num
        return True
        
