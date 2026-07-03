# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(treeA, treeB):
            if not treeA and not treeB:
                return True
            
            if not treeA or not treeB or treeA.val != treeB.val:
                return False
            
            return same(treeA.left, treeB.left) and same(treeA.right, treeB.right)

        
        def dfs(node):
            if not node:
                return False
            

            if same(node, subRoot):
                return True


            return dfs(node.left) or dfs(node.right)

        return dfs(root)