from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        my_map = defaultdict(list)
        if not nums:
            return 0
        for num in nums:
            my_map[num].append(num)
        res = 1
        for num in nums:
            if (num + 1) not in my_map:
                longest = 1
                while (num - longest) in my_map:
                    longest += 1
                res = max(res, longest)

        return res
                    

