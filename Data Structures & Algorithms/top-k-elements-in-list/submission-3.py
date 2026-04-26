class Solution:
    # 
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     hash_map = {item: 0 for item in nums}
    #     for item in nums:
    #         hash_map[item] += 1
    #     # Sort by value in descending order
    #     sorted_items = sorted(hash_map.items(),key=lambda x: x[1], reverse=True)
    #     # print(sorted_items)
    #     # print(hash_map.sort)
    #     res = []
    #     for i in range(k):
    #         res.append(sorted_items[i][0])
    #     # prrint(res)
    #     return res
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)

        heap = []

        for item in my_map:
            heapq.heappush(heap, (my_map[item], item))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res

        