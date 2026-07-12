class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        freq_table = [[] for i in range(len(nums) + 1)]


        for num in nums:
            counter_map[num] = 1 + counter_map.get(num, 0)
        
        for key in counter_map:
            freq_table[counter_map[key]].append(key)

        res = []
        for elem in reversed(freq_table):
            for i in elem:
                if len (res) == k:
                    return res
                res.append(i)

        return res