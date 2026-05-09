import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for item, value in counter.items():
            heapq.heappush(heap, [value, item])
            print(item, value)

        len_h = len(heap)

        while len_h > k:
            heapq.heappop(heap)
            len_h -= 1

        res = []
        for item in heap:
            res.append(item[1])

        return res

