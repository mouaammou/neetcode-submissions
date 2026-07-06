# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return None
        count = 0

        def dfs (node, max_so_far):
            if not node:
                return 
            nonlocal count
            if node.val >= max_so_far:
                count += 1
            
            maxium = max(node.val, max_so_far)
            dfs(node.left, maxium)
            dfs(node.right, maxium)

        dfs(root, root.val)
        return count



