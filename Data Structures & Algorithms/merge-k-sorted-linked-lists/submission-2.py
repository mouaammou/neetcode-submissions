# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        # add first heads to the heap
        heap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(heap, (lists[i].val, i, lists[i]))


        while heap:
            #pop the smallest one from the heap
            value, index, min_node  = heapq.heappop(heap)

            curr.next = min_node
            curr = curr.next

            # add the next node that follow the smallest node
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, index, min_node.next))

        return res.next