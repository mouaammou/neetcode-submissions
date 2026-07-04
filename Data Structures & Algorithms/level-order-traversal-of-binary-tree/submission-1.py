# Definition for a binary tree node.
# class TreeNode:
#     def __init__(Deque, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            new_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                new_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(new_list)

          

        return res
