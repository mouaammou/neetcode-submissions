"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        nodes_map = {}

        curr = head

        while curr:
            new_node = Node(curr.val)

            nodes_map[curr] = new_node

            curr = curr.next

        
        curr = head

        while curr:
            nodes_map[curr].next = nodes_map.get(curr.next)
            nodes_map[curr].random = nodes_map.get(curr.random)

            curr = curr.next

        return nodes_map[head]