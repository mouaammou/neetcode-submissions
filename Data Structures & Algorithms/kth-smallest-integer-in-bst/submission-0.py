# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        counter = 0
        res = 0
        def inorder(node):
            if not node:
                return None
            nonlocal counter
            nonlocal res
            inorder(node.left)
            counter += 1
            if counter == k:
                res = node.val
            inorder(node.right)

        inorder(root)
        return res
