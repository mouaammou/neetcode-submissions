class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        res = []

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        new_list = sorted(freq_map.items(), key=lambda item: item[1])
        
        for key in reversed(new_list):
            res.append(key[0])
            if len(res) == k:
                break
        return res

