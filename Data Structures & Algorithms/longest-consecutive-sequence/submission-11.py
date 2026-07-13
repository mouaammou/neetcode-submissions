class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        logest_map = {i: 1 for i in nums}

        res = 0
        for num in nums:
            j = num - 1
            r = 1
            while j in logest_map:
                
                r += 1
                j -= 1
            res = max(res, r)   
        return res