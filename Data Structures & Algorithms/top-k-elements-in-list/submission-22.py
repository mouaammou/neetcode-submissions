from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for num in nums:
            my_map[num] += 1

        res = []
        for key, value in my_map.items():
            res.append((key, value))

        res.sort(key=lambda x: x[1], reverse=True)

        return_val = []
        i = 0
        while i < k:
            return_val.append(res[i][0])
            i += 1

        return return_val


        