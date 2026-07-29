from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            my_map[num] += 1

        for key, value in my_map.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        




        